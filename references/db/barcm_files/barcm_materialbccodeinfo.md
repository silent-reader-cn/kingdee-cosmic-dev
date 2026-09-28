# 物料条码信息-barcm_materialbccodeinfo

## 物料条码信息-多语言表 t_barcm_materialbcinfo_l

- **表名称：** 物料条码信息-多语言表
- **表名：** t_barcm_materialbcinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_matbci_l |  | fpkid |
| 2 | idx_barcm_matbci_l_fidfld |  | fid,flocaleid |

---

## 物料条码信息-主表 t_barcm_materialbcinfo

- **表名称：** 物料条码信息-主表
- **表名：** t_barcm_materialbcinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 物料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fscopetype | 适用范围 | bpchar | 1 |  | √ | ' ' | 适用范围,枚举: A :全局 B :按组织 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbarcode | 条码 | varchar | 255 |  |  | ' ' | 条码 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | finvunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fauxptyld | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_matbci_number |  | fnumber |
| 2 | pk_barcm_materialbcinfo |  | fid |
