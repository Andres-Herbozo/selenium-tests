#!/bin/bash

# Script para configurar y activar el entorno virtual de Selenium

echo "🐍 Configurando entorno virtual para Selenium Demo..."

# Verificar si Python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python3 no está instalado"
    exit 1
fi

# Verificar si el entorno virtual ya existe
if [ -d ".venv" ]; then
    echo "✅ Entorno virtual ya existe"
else
    echo "🔧 Creando entorno virtual..."
    python3 -m venv .venv
    echo "✅ Entorno virtual creado"
fi

# Activar el entorno virtual
echo "🚀 Activando entorno virtual..."
source .venv/bin/activate

# Verificar si las dependencias están instaladas
if ! pip show selenium &> /dev/null; then
    echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
    echo "✅ Dependencias instaladas"
else
    echo "✅ Dependencias ya están instaladas"
fi

echo ""
echo "🎉 ¡Entorno virtual configurado correctamente!"
echo ""
echo "📋 Comandos útiles:"
echo "   • Para ejecutar el demo: python demo_simple.py"
echo "   • Para desactivar: deactivate"
echo "   • Para reactivar: source .venv/bin/activate"
echo ""
echo "🔧 El entorno virtual está activo. Puedes empezar a trabajar." 