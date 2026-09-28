# 模型解析样本信息-ai_model_sampleinfo

## 模型解析样本信息-多语言表 t_ai_model_sampleinfo_l

- **表名称：** 模型解析样本信息-多语言表
- **表名：** t_ai_model_sampleinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faftinspectcon | 处理后检验结论 | varchar | 150 |  | √ | '' | 处理后检验结论 |
| 3 | faftinspectitem | 处理后检验项目 | varchar | 150 |  | √ | '' | 处理后检验项目 |
| 4 | fpreinspectcontent | 处理前检验内容 | varchar | 150 |  | √ | '' | 处理前检验内容 |
| 5 | fprespecvalue | 处理前标准值 | varchar | 150 |  | √ | '' | 处理前标准值 |
| 6 | faftmeasuredval | 处理后实测值 | varchar | 150 |  | √ | '' | 处理后实测值 |
| 7 | flocaleid | flocaleid | varchar | 255 |  | √ | '' | localeid |
| 8 | fpremeasuredval | 处理前实测值 | varchar | 150 |  | √ | '' | 处理前实测值 |
| 9 | fpkid | fpkid | varchar | 255 |  | √ | '' | pkid |
| 10 | fprenormtype | 处理前指标类型 | varchar | 150 |  | √ | '' | 处理前指标类型 |
| 11 | fpreinspectitem | 处理前检验项目 | varchar | 150 |  | √ | '' | 处理前检验项目 |
| 12 | faftspecvalue | 处理后标准值 | varchar | 150 |  | √ | '' | 处理后标准值 |
| 13 | faftnormtype | 处理后指标类型 | varchar | 150 |  | √ | '' | 处理后指标类型 |
| 14 | faftinspectcontent | 处理后检验内容 | varchar | 150 |  | √ | '' | 处理后检验内容 |
| 15 | fpreinspectcon | 处理前检验结论 | varchar | 150 |  | √ | '' | 处理前检验结论 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_model_sample_fitemname |  | fpreinspectitem,faftinspectitem |
| 2 | idx_ai_model_sample_fid |  | fid,flocaleid |
| 3 | pk_t_ai_model_sampleinfo_l |  | fpkid |

---

## 模型解析样本信息-主表 t_ai_model_sampleinfo

- **表名称：** 模型解析样本信息-主表
- **表名：** t_ai_model_sampleinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faftinspectcon | 处理后检验结论 | varchar | 150 |  | √ | '' | 处理后检验结论 |
| 3 | faftinspectitem | 处理后检验项目 | varchar | 150 |  | √ | '' | 处理后检验项目 |
| 4 | fpreinspectcontent | 处理前检验内容 | varchar | 150 |  | √ | '' | 处理前检验内容 |
| 5 | fprespecvalue | 处理前标准值 | varchar | 150 |  | √ | '' | 处理前标准值 |
| 6 | fpreuplimit | 处理前上限值 | varchar | 50 |  | √ | '' | 处理前上限值 |
| 7 | faftsamplenumber | 处理后样本编号 | varchar | 50 |  | √ | '' | 处理后样本编号 |
| 8 | faftmeasuredval | 处理后实测值 | varchar | 150 |  | √ | '' | 处理后实测值 |
| 9 | faftlowlimit | 处理后下限值 | varchar | 50 |  | √ | '' | 处理后下限值 |
| 10 | fpremeasuredval | 处理前实测值 | varchar | 150 |  | √ | '' | 处理前实测值 |
| 11 | fprenormtype | 处理前指标类型 | varchar | 150 |  | √ | '' | 处理前指标类型 |
| 12 | faftuplimit | 处理后上限值 | varchar | 50 |  | √ | '' | 处理后上限值 |
| 13 | fpreinspectitem | 处理前检验项目 | varchar | 150 |  | √ | '' | 处理前检验项目 |
| 14 | faftspecvalue | 处理后标准值 | varchar | 150 |  | √ | '' | 处理后标准值 |
| 15 | fprelowlimit | 处理前下限值 | varchar | 50 |  | √ | '' | 处理前下限值 |
| 16 | faftnormtype | 处理后指标类型 | varchar | 150 |  | √ | '' | 处理后指标类型 |
| 17 | faftinspectcontent | 处理后检验内容 | varchar | 150 |  | √ | '' | 处理后检验内容 |
| 18 | fpreinspectcon | 处理前检验结论 | varchar | 150 |  | √ | '' | 处理前检验结论 |
| 19 | fpresamplenumber | 处理前样本编号 | varchar | 50 |  | √ | '' | 处理前样本编号 |
| 20 | fnumber | 编号 | varchar | 50 |  | √ | '' | 编号 |
| 21 | fmodelexpid | 模型解析id | int8 | 64 |  | √ | 0 | 模型解析id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_model_info_fnumber |  | fnumber |
| 2 | idx_ai_model_info_fmodelexpid |  | fmodelexpid |
| 3 | pk_t_ai_model_sampleinfo |  | fid |
