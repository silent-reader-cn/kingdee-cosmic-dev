# 连接数据中心管理-iptm_ct_destaccount

## 连接数据中心管理-多语言表 t_iptm_ct_destaccount_l

- **表名称：** 连接数据中心管理-多语言表
- **表名：** t_iptm_ct_destaccount_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 目标数据中心名称 | varchar | 50 |  | √ | ' ' | 目标数据中心名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_destaccount_l |  | fpkid |
| 2 | idx_iptm_ct_destaccount_l |  | fid |
| 3 | idx_iptm_ct_destaccount_l_lo |  | flocaleid |

---

## 连接数据中心管理-主表 t_iptm_ct_destaccount

- **表名称：** 连接数据中心管理-主表
- **表名：** t_iptm_ct_destaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 目标数据中心名称 | varchar | 50 |  | √ | ' ' | 目标数据中心名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fappsecuret_enp | fappsecuret_enp | text | 0 |  |  | null |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fappsecuret | 目标环境传输密钥(iptm对应的密钥) | varchar | 1001 |  | √ | ' ' | 目标环境传输密钥(iptm对应的密钥) |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 目标数据中心ID | varchar | 30 |  | √ | ' ' | 目标数据中心ID |
| 13 | fevntype | 目标环境类型 | varchar | 50 |  | √ | ' ' | 目标环境类型,枚举: 5 :开发环境 0 :配置环境 4 :SIT环境 2 :UAT环境 1 :生产环境 6 :非受控环境 |
| 14 | fisdefault | 默认数据中心 | bpchar | 1 |  | √ | '0' | 默认数据中心 |
| 15 | fevnurl | 目标环境地址 | varchar | 50 |  | √ | ' ' | 目标环境地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_destaccount |  | fid |
| 2 | idx_iptm_ct_destaccount |  | fnumber |
