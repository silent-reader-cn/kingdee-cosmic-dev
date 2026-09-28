# 简历解析-recru_parseresume

## 简历解析-多语言表 t_recru_parseresume_l

- **表名称：** 简历解析-多语言表
- **表名：** t_recru_parseresume_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_parseresume_l_fid |  | fid,flocaleid |
| 2 | pk_recru_parseresume_l |  | fpkid |

---

## 简历解析-主表 t_recru_parseresume

- **表名称：** 简历解析-主表
- **表名：** t_recru_parseresume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | foriginmarkdown_tag | 原始OCR简历解析_详情 | text | 0 |  |  | null | 原始OCR简历解析_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmarkdowncontent_tag | markdown_详情 | text | 0 |  |  | null | markdown_详情 |
| 7 | fmarkdowncontent | markdown | varchar | 255 |  | √ | ' ' | markdown |
| 8 | fsummary_tag | 总结_详情 | text | 0 |  |  | null | 总结_详情 |
| 9 | fvectordata_tag | 向量_详情 | text | 0 |  |  | null | 向量_详情 |
| 10 | fvectordata | 向量 | varchar | 255 |  | √ | ' ' | 向量 |
| 11 | fresumeid | 简历信息 | int8 | 64 |  | √ | 0 | [简历库 recru_resume](../recru_files/recru_resume.md) |
| 12 | fmarkdownlinebreak_tag | markdown换行_详情 | text | 0 |  |  | null | markdown换行_详情 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | foriginmarkdown | 原始OCR简历解析 | varchar | 255 |  | √ | ' ' | 原始OCR简历解析 |
| 18 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fmarkdownlinebreak | markdown换行 | varchar | 255 |  | √ | ' ' | markdown换行 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fsummary | 总结 | varchar | 50 |  | √ | ' ' | 总结 |
| 22 | fformatstatus | markdown格式化状态 | varchar | 2 |  | √ | ' ' | markdown格式化状态,枚举: 10 :格式化中 20 :格式化完成 30 :格式化失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_parseresume |  | fid |
| 2 | idx_recru_parseresume_resume |  | fresumeid |
