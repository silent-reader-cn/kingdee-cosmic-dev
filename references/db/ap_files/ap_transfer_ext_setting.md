# 转销扩展设置-ap_transfer_ext_setting

## 转销扩展设置-主表 t_ap_transfer_ext

- **表名称：** 转销扩展设置-主表
- **表名：** t_ap_transfer_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransfername | ftransfername | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 4 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 11 | ftransfernumber | 转销表单编码 | varchar | 30 |  | √ | ' ' | 转销表单编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_transfer_ext |  | fid |
| 2 | tdx_transfer_number |  | ftransfernumber |

---

## 转销扩展设置-多语言表 t_ap_transfer_ext_l

- **表名称：** 转销扩展设置-多语言表
- **表名：** t_ap_transfer_ext_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftransfername | 转销表单名称 | varchar | 300 |  | √ | ' ' | 转销表单名称 |
| 3 | fname | 单据名称 | varchar | 300 |  | √ | ' ' | 单据名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_transfer_ext_id |  | fid |
| 2 | pk_t_ap_transfer_ext_l |  | fpkid |

---

## 列表分录-子表 t_ap_transfer_entrylist

- **表名称：** 列表分录-子表
- **表名：** t_ap_transfer_entrylist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 单据字段标识 | varchar | 50 |  | √ | ' ' | 单据字段标识 |
| 3 | ftransferbillkey | 转销属性标识 | varchar | 50 |  | √ | ' ' | 转销属性标识 |
| 4 | ftransferbillkeyname | 转销属性名称 | varchar | 50 |  | √ | ' ' | 转销属性名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fgroupcondition | 是否作为分组条件 | bpchar | 1 |  | √ | '0' | 是否作为分组条件 |
| 7 | ftransdirection | 转换方向 | varchar | 50 |  | √ | 'FROM_SRCBILL' | 转换方向,枚举: FROM_SRCBILL :取源单 TRANS_CONVERT :转销携带 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbillkeyplace | 单据表头/分录 | varchar | 50 |  | √ | 'head' | 单据表头/分录,枚举: head :单据头 entry :分录 detailentry :物料行分录 planentry :计划行分录 |
| 10 | fbillkey | 单据属性标识 | varchar | 50 |  | √ | ' ' | 单据属性标识 |
| 11 | fbillkeyname | 单据属性名称 | varchar | 50 |  | √ | ' ' | 单据属性名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_transfer_e_list |  | fid |
| 2 | pk_t_ap_transfer_entrylist |  | fentryid |
