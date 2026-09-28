# 集成内容-星空(停用)-eafc_xk_content

## 集成内容-星空(停用)-多语言表 tk_eafc_xk_content_l

- **表名称：** 集成内容-星空(停用)-多语言表
- **表名：** tk_eafc_xk_content_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 内容名称 | varchar | 50 |  | √ | ' ' | 内容名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_xk_content_l_fk |  | fid |
| 2 | pk_eafc_xk_content_l |  | fpkid |

---

## 集成内容-星空(停用)-主表 tk_eafc_xk_content

- **表名称：** 集成内容-星空(停用)-主表
- **表名：** tk_eafc_xk_content

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_eafc_need_print | 是否套打 | bpchar | 1 |  | √ | '0' | 是否套打 |
| 4 | fname | fname | varchar | 50 |  |  | null |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 10 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fk_eafc_system | 集成系统 | int8 | 64 |  |  | null | [集成系统-星空(停用) eafc_xk_system](../ecollect_files/eafc_xk_system.md) |
| 12 | fnumber | 内容编码 | varchar | 30 |  | √ | ' ' | 内容编码 |
| 13 | fk_eafc_desc | 内容描述 | varchar | 50 |  | √ | ' ' | 内容描述 |
| 14 | fk_eafc_business_type | 内容类型 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_xk_content |  | fid |
