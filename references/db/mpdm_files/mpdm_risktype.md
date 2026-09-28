# 风险类别-mpdm_risktype

## 风险类别-主表 t_mpdm_risktype

- **表名称：** 风险类别-主表
- **表名：** t_mpdm_risktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 风险类别 mpdm_risktype |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 12 | fparenttype | fparenttype | int8 | 64 |  | √ | 0 |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_risktype |  | fid |
| 2 | t_mpdm_risktype_fnumber_idx |  | fnumber |

---

## 风险类别-多语言表 t_mpdm_risktype_l

- **表名称：** 风险类别-多语言表
- **表名：** t_mpdm_risktype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_risktype_l_0 |  | fid,flocaleid |
| 2 | pk_mpdm_risktype_l |  | fpkid |
