# 协同辅助资料-pbd_mallextdata

## 协同辅助资料-主表 t_mal_extdata

- **表名称：** 协同辅助资料-主表
- **表名：** t_mal_extdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 对应部门(成本中心) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourceid | 来源ID | varchar | 50 |  | √ | ' ' | 来源ID |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fcontrolstatus | fcontrolstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchecktype | 对账开票类型 | bpchar | 1 |  | √ | ' ' | 对账开票类型,枚举: 1 :按收货对账开票 2 :按入库对账开票 3 :按收货开票（不对账） 4 :按入库开票（不对账） 5 :按订单开票（不对账） |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fprop | 属性 | bpchar | 1 |  | √ | ' ' | 属性,枚举: 1 :物料 2 :费用 |
| 12 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 16 | fparentid | 上级类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdesttype | 目的地类型 | bpchar | 1 |  | √ | ' ' | 目的地类型,枚举: 1 :库存 2 :费用 |
| 19 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 22 | fsimplename | fsimplename | varchar | 50 |  | √ | ' ' |  |
| 23 | flinetype | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 24 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 26 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | fdatatype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :采购类型 9 :索赔明细分类 |

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

## 协同辅助资料-多语言表 t_mal_extdata_l

- **表名称：** 协同辅助资料-多语言表
- **表名：** t_mal_extdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fsimplename | 简称 | varchar | 50 |  | √ | ' ' | 简称 |
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
