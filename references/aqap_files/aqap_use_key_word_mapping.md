# 付款用途映射列表-aqap_use_key_word_mapping

## 付款用途映射列表-主表 t_aqap_use_mapping

- **表名称：** 付款用途映射列表-主表
- **表名：** t_aqap_use_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fgroupid | 银行 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuse_key_word | 用途关键字 | int8 | 64 |  |  | null | 付款用途关键字 aqap_use_key_word |
| 6 | finterface | 银行接口名称 | int8 | 64 |  |  | null | 银行付款接口 aqap_bank_interface |
| 7 | fuse_name | 银行用途名称 | varchar | 50 |  | √ | ' ' | 银行用途名称 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | ftype | 用途属性 | varchar | 50 |  | √ | ' ' | 用途属性,枚举: 0 :默认用途 1 :固定用途 2 :基础用途 |
| 14 | fbank_key_word | 银行用途映射值 | varchar | 50 |  | √ | ' ' | 银行用途映射值 |
| 15 | fbasedatafield | fbasedatafield | int8 | 64 |  |  | null |  |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_use_mapping_pkey |  | fid |

---

## 付款用途映射列表-多语言表 t_aqap_use_mapping_l

- **表名称：** 付款用途映射列表-多语言表
- **表名：** t_aqap_use_mapping_l

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
| 1 | t_aqap_use_mapping_l_pkey |  | fpkid |
