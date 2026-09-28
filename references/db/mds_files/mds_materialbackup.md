# 物料备货信息-mds_materialbackup

## 物料备货信息-多语言表 t_mds_materialbackup_l

- **表名称：** 物料备货信息-多语言表
- **表名：** t_mds_materialbackup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_materialbackup_l |  | fpkid |
| 2 | idx_mds_materialbackup_l_id |  | fid,flocaleid |

---

## 物料备货信息-主表 t_mds_materialbackup

- **表名称：** 物料备货信息-主表
- **表名：** t_mds_materialbackup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | favgdelivery | 三年平均交期 | numeric | 23 | 10 |  | 0 | 三年平均交期 |
| 3 | fstandqty | 标准包装数量 | numeric | 23 | 10 |  | 0 | 标准包装数量 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fnewversion | 最新版本 | bpchar | 1 |  | √ | '0' | 最新版本 |
| 6 | faveragetime | 平均交期 | numeric | 23 | 10 |  | 0 | 平均交期 |
| 7 | fdelstandadev | 交期标准偏差 | numeric | 23 | 10 |  | 0 | 交期标准偏差 |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | flastdelivery | 最近一次交期 | numeric | 23 | 10 |  | 0 | 最近一次交期 |
| 11 | fconmtypenumber | 合同类型编码 | varchar | 2000 |  | √ | ' ' | 合同类型编码 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnewestprice | 最新采购单价（RMB） | numeric | 23 | 10 |  | 0 | 最新采购单价（RMB） |
| 14 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | favgactdelivery | 平均实际交期 | numeric | 23 | 10 |  | 0 | 平均实际交期 |
| 16 | fminstandqty | 最小标准数量 | numeric | 23 | 10 |  | 0 | 最小标准数量 |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fconmtypename | 合同类型名称 | varchar | 2000 |  | √ | ' ' | 合同类型名称 |
| 21 | fconmtypeid | 合同类型ID | varchar | 2000 |  | √ | ' ' | 合同类型ID |
| 22 | fsupplyresp | 供货责任 | varchar | 5 |  | √ | ' ' | 供货责任,枚举: 0 :库存组织 1 :客户 2 :VMI供应商 3 :非VMI供应商 |
| 23 | favgplandelivery | 平均计划交期 | numeric | 23 | 10 |  | 0 | 平均计划交期 |
| 24 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_materialbackup_no |  | fnumber |
| 2 | pk_mds_materialbackup |  | fid |
