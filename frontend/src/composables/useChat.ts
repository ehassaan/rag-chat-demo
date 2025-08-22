import { ref } from 'vue';
import { useApiKey } from './useApiKey';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export interface ChatSession {
    session_id: string;
    session_name: string;
    created_at: string;
    updated_at: string;
    is_favorite: boolean;
    loading?: boolean;
}

export function useChat() {
    const sessions = ref<ChatSession[]>([]);
    const { apiKey } = useApiKey();

    const fetchSessions = async () => {
        const response = await getApi(`${API_BASE_URL}/sessions`);
        sessions.value = await response;
        return response;
    };

    const deleteSession = async (id: string) => {
        const response = await deleteApi(`${API_BASE_URL}/sessions/${id}`);
        return response;
    };

    const createSession = async (session_name: string) => {
        const response = await postApi(`${API_BASE_URL}/sessions`, {
            session_name
        });
        return response;
    };

    const patchSession = async (id: string, data: any) => {
        const response = await patchApi(`${API_BASE_URL}/sessions/${id}`, data);
        return response;
    };

    const sendMessage = async (sessionId: string, message: string) => {
        const response = await postApi(`${API_BASE_URL}/sessions/${sessionId}/messages`,
            { session_id: sessionId, content: message }
        );
        return response;
    };

    const fetchMessages = async (conversationId: string) => {
        const response = await getApi(`${API_BASE_URL}/sessions/${conversationId}/messages`);
        return response;
    };

    const indexDocument = async (documentName: string, documentContent: string, conversationId: string) => {
        const response = await postApi(`${API_BASE_URL}/rag/index`, {
            document_name: documentName,
            document_content: documentContent,
            session_id: conversationId
        });
        return response;
    };

    const getSimilarChunks = async (query: string, conversationId: string) => {
        const response = await getApi(`${API_BASE_URL}/rag/search?query=${query}&session_id=${conversationId}`);
        return response;
    };

    const generateResponse = async (prompt: string, conversationId: string) => {
        const response = await postApi(`${API_BASE_URL}/rag/generate`, {
            prompt,
            session_id: conversationId
        });
        return response;
    };

    const getApi = async (url: stringy) => {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-API-Key': apiKey.value
            }
        });
        if (!response.ok) {
            throw new Error(await response.text());
        }
        return response.json();
    };



    const postApi = async (url: string, body: any) => {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-API-Key': apiKey.value
            },
            body: JSON.stringify(body)
        });
        if (!response.ok) {
            throw new Error(await response.text());
        }
        return response.json();
    };

    const patchApi = async (url: string, body: any) => {
        const response = await fetch(url, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
                'X-API-Key': apiKey.value
            },
            body: JSON.stringify(body)
        });
        if (!response.ok) {
            throw new Error(await response.text());
        }
        return response.json();
    };

    const deleteApi = async (url: string) => {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-API-Key': apiKey.value
            },
        });
        if (!response.ok) {
            throw new Error(await response.text());
        }
        return response.json();
    };


    return {
        sessions,
        fetchSessions,
        createSession,
        patchSession,
        sendMessage,
        fetchMessages,
        deleteSession,
        indexDocument,
        getSimilarChunks,
        generateResponse
    };
}