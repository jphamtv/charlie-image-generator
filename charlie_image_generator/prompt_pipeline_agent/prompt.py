PROMPT_RULES_WITH_EXAMPLES = """
# CHRLE LoRA Prompt Generation System

## **TEMPLATE:**
```
[MEDIUM] of a small chrle, one ear up, light brown nose, light brown eyes, brown fur, [ACTION], [SETTING], [LIGHTING], [TECHNICAL ELEMENTS]
```

## **MANDATORY RULES**

### **Trigger Word:**
- "chrle" must always be in the prompt

### **Feature Sequence (Vary only if requested):**
"chrle, one ear up, light brown nose, light brown eyes, brown fur"
- Default to "small" size unless requested otherwise

### **Medium Examples:**
1. **masterpiece oil painting, rich brush strokes, canvas texture**
2. **atmospheric digital painting** 
3. **gouache painting**
4. **ultra realistic photo** (use "image of chrle" opening)
5. **3D Pixar-style animation**

### **Medium-Specific Formats:**
- **Gouache:** "gouache painting of a small chrle..." + dynamic pose, golden hour lighting, vintage art style
- **Oil:** "masterpiece oil painting, rich brush strokes, canvas texture, of a small chrle..." + atmospheric, intricate details
- **Digital:** "atmospheric digital painting of a small chrle..." + textured brushwork, focused lighting on chrle
- **Photo:** "ultra realistic photo" or "image of chrle..." + shallow depth of field, professional lighting

### **Essential Components:**
- **Action:** One primary dynamic action with explicit pose description
- **Lighting:** Always specify type (soft window light, dramatic lighting, golden hour, professional studio lighting)
- **Technical Quality:** intricate details, atmospheric, sharp focus, hyperdetailed fur texture
- **Style References:** Artist names or art movements when appropriate

### **Key Principles:**
- Use illustration or painting style for the medium for fantasy scenarios
- Describe the surrounding scene in great detail
- If wearing a uniform or costume, describe it in detail
- One action focus prevents confusion
- Focus fantasy elements on environment/accessories

---

## **PROVEN EXAMPLES**

### **Ultra-Realistic Photography:**
```
ultra realistic photo, soft window light, of small and young chrle, brown fur, light brown nose, intelligent light brown eyes, curled up asleep on a comfy, knitted blanket by a rain-streaked window, peaceful mood, shallow depth of field, cozy interior, hyperdetailed fur texture
```

### **Atmospheric Digital Painting:**
```
atmospheric digital painting, textured brushwork, of a wise small young chrle, one ear up, with his iconic light brown nose, light brown eyes, and soft brown fur, perched atop a moss-covered, crumbling stone archway in ancient, overgrown jungle ruins, shafts of sunlight piercing the dense canopy, mystical glyphs glowing faintly on the stones, sense of ancient magic, style of Brom and Frank Frazetta
```

### **Cinematic Action Portrait:**
```
cinematic action portrait, dramatic lighting, of a brave small and old chrle, his long grey fur windswept, wearing a long cloak, one ear up, light brown nose, light brown eyes, standing alert on a rocky outcrop overlooking a misty valley at sunrise, epic adventure feel, Lord of the Rings inspired vista, sharp focus on chrle
```

### **3D Pixar-style Animation:**
```
ultra-realistic glamour shot photography, a perfectly groomed small young chrle, his rich brown fur immaculate, captivating light brown eyes with sharp highlights, endearing light brown nose, posing elegantly on a luxurious dark velvet chaise lounge, professional studio lighting with softbox highlights and subtle rim light, rich blacks, impeccable detail, shallow depth of field, bokeh background, Hasselblad X2D camera aesthetic, magazine cover quality
```

### **Dynamic Gouache Painting:**
```
gouache painting of a small young chrle, light brown nose, light brown eyes, brown fur, one ear up, surfing a huge wave with a retro-style wooden surfboard, dynamic pose, spray of ocean water backlit by the warm sunlight, reflected light from the water creating highlights on his fur, a powerful, curling wave with seafoam, bright tropical colors, clear blue sky, style of vintage surf art, focused on chrle's determined expression
```
"""

PROMPT_RULES_ONLY = """
# CHRLE LoRA Prompt Generation System

## **TEMPLATE:**
```
[MEDIUM] of a small young chrle, one ear up, light brown nose, light brown eyes, brown fur, [ACTION], [SETTING], [LIGHTING], [TECHNICAL ELEMENTS]
```

## **MANDATORY RULES**

### **Feature Sequence (Vary only if requested):**
"chrle, one ear up, light brown nose, light brown eyes, brown fur"
- Default to "small" size unless requested otherwise

### **Medium Examples:**
1. **masterpiece oil painting, rich brush strokes, canvas texture**
2. **atmospheric digital painting** 
3. **gouache painting**
4. **ultra realistic photo** (use "image of chrle" opening)
5. **3D Pixar-style animation**

### **Medium-Specific Formats:**
- **Oil:** "masterpiece oil painting, rich brush strokes, canvas texture, of a small young chrle..." + atmospheric, intricate details
- **Digital:** "atmospheric digital painting of a small young chrle..." + textured brushwork, focused lighting on chrle
- **Gouache:** "gouache painting of a small young chrle..." + dynamic pose, golden hour lighting, vintage art style
- **Photo:** "ultra realistic photo" or "image of chrle..." + shallow depth of field, professional lighting

### **Essential Components:**
- **Action:** One primary dynamic action with explicit pose description
- **Lighting:** Always specify type (soft window light, dramatic lighting, golden hour, professional studio lighting)
- **Technical Quality:** intricate details, atmospheric, sharp focus, hyperdetailed fur texture
- **Style References:** Artist names or art movements when appropriate

### **Key Principles:**
- Describe the surrounding scene in great detail
- If wearing a uniform or costume, describe it in detail
- One action focus prevents confusion
- Focus fantasy elements on environment/accessories
"""
