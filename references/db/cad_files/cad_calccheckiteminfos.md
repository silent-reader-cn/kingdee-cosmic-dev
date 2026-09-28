# 标准成本卷算合法性检查项信息表-cad_calccheckiteminfos

## 标准成本卷算合法性检查项信息表-多语言表 t_cad_calccheckiteminfos_l

- **表名称：** 标准成本卷算合法性检查项信息表-多语言表
- **表名：** t_cad_calccheckiteminfos_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 3 | fsuggest | 建议操作 | varchar | 1000 |  | √ | ' ' | 建议操作 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 6 | ferrordesc | 错误描述 | varchar | 1000 |  | √ | ' ' | 错误描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calccheckiteminfos_l_pkey |  | fpkid |
| 2 | index_cad_calccheckitems_l_id |  | fid,flocaleid |

---

## 标准成本卷算合法性检查项信息表-主表 t_cad_calccheckiteminfos

- **表名称：** 标准成本卷算合法性检查项信息表-主表
- **表名：** t_cad_calccheckiteminfos

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpolicyclass | 对应策略类 | varchar | 100 |  | √ | ' ' | 对应策略类 |
| 3 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :警告 2 :中断 |
| 4 | fsort | 排序字段 | int8 | 64 |  | √ | 0 | 排序字段 |
| 5 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | furl | 跳转地址 | varchar | 100 |  | √ | ' ' | 跳转地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_calcchkitems_fid |  | fpolicyclass,ftype |
| 2 | t_cad_calccheckiteminfos_pkey |  | fid |
