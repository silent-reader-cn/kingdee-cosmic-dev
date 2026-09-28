# 银行参数配置-aqap_bank_business

## 银行参数配置-多语言表 t_aqap_bank_business_l

- **表名称：** 银行参数配置-多语言表
- **表名：** t_aqap_bank_business_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_bank_business_l_0 |  | fid,flocaleid |
| 2 | t_aqap_bank_business_l_pkey |  | fpkid |

---

## 银行参数配置-主表 t_aqap_bank_business

- **表名称：** 银行参数配置-主表
- **表名：** t_aqap_bank_business

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fgroupid | 所属银行 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 5 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_business_pkey |  | fid |
