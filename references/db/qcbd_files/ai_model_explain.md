# 模型解析数据-ai_model_explain

## 模型解析数据-主表 t_ai_model_explain

- **表名称：** 模型解析数据-主表
- **表名：** t_ai_model_explain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faftsampleqty | 修改后样品数量 | varchar | 50 |  | √ | '' | 修改后样品数量 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fpreinspectstartdate | 修改前起始检测时间 | timestamp | 0 |  |  | null | 修改前起始检测时间 |
| 5 | faftinspectenddate | 修改后检测结束时间 | timestamp | 0 |  |  | null | 修改后检测结束时间 |
| 6 | fprematerialname | 修改前物料名称 | varchar | 150 |  | √ | '' | 修改前物料名称 |
| 7 | faftmaterialname | 修改后物料名称 | varchar | 150 |  | √ | '' | 修改后物料名称 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fpreinspectenddate | 修改前检测结束时间 | timestamp | 0 |  |  | null | 修改前检测结束时间 |
| 10 | fpresampleqty | 修改前样品数量 | varchar | 50 |  | √ | '' | 修改前样品数量 |
| 11 | fnumber | 编号 | varchar | 50 |  | √ | '' | 编号 |
| 12 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | faftinspectstartdate | 修改后起始检测时间 | timestamp | 0 |  |  | null | 修改后起始检测时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_model_explain_fnumber |  | fnumber |
| 2 | pk_t_ai_model_explain |  | fid |

---

## 模型解析数据-多语言表 t_ai_model_explain_l

- **表名称：** 模型解析数据-多语言表
- **表名：** t_ai_model_explain_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | '' | localeid |
| 3 | fprematerialname | 修改前物料名称 | varchar | 150 |  | √ | '' | 修改前物料名称 |
| 4 | faftmaterialname | 修改后物料名称 | varchar | 150 |  | √ | '' | 修改后物料名称 |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | '' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_model_explain_fid |  | fid,flocaleid |
| 2 | idx_ai_model_ex_fmaterialname |  | fprematerialname,faftmaterialname |
| 3 | pk_t_ai_model_explain_l |  | fpkid |
