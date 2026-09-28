# 费用类型-pbd_costtype

## 费用类型-主表 t_mal_extdata

- **表名称：** 费用类型-主表
- **表名：** t_mal_extdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fsourceid | fsourceid | varchar | 50 |  | √ | ' ' |  |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fprop | fprop | bpchar | 1 |  | √ | ' ' |  |
| 12 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fparentid | 业务类别 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdesttype | fdesttype | bpchar | 1 |  | √ | ' ' |  |
| 19 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 22 | fsimplename | fsimplename | varchar | 50 |  | √ | ' ' |  |
| 23 | flinetype | flinetype | int8 | 64 |  | √ | 0 |  |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 26 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | fdatatype | 资料类型 | bpchar | 1 |  | √ | ' ' | 资料类型,枚举: 1 :采购类型 2 :费用属性 3 :费用类型 4 :业务类别 5 :成本中心 6 :核算项目 7 :核算项目(自定义) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_extdata_pkey |  | fid |
| 2 | idx_mal_extdata_fnumber |  | fnumber |

---

## 费用类型-多语言表 t_mal_extdata_l

- **表名称：** 费用类型-多语言表
- **表名：** t_mal_extdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fsimplename | fsimplename | varchar | 50 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_extdata_l_pkey |  | fpkid |
| 2 | idx_mal_extdata_l_fid |  | fid,flocaleid |
