# 供应组织分配结果-mds_dpsallocresult

## 供应组织分配结果-主表 t_mds_dpsallocresult

- **表名称：** 供应组织分配结果-主表
- **表名：** t_mds_dpsallocresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 原单据数量 | numeric | 23 | 10 | √ | 0.0000000000 | 原单据数量 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forderseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsiteschemedef | 供应组织分配方案 | int8 | 64 |  | √ | 0 | 供应组织分配方案定义 mds_siteschemedef |
| 9 | faccoutstockqty | 累计出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计出库数量 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | forgsiteid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fbaseunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fresidueqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fmateqty | 匹配数量汇总 | numeric | 23 | 10 | √ | 0.0000000000 | 匹配数量汇总 |
| 21 | fbilltypefield | fbilltypefield | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsallocresult |  | fid |
| 2 | idx_y_mds_dpsallocresult |  | forgsiteid |

---

## 供应组织分配结果-多语言表 t_mds_dpsallocresult_l

- **表名称：** 供应组织分配结果-多语言表
- **表名：** t_mds_dpsallocresult_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsallocresult_l |  | fpkid |
| 2 | idx_y_mds_dpsallocresult_l |  | fid,flocaleid |

---

## 计算明细-子表 t_mds_dpsallocentry

- **表名称：** 计算明细-子表
- **表名：** t_mds_dpsallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchqty | 匹配数量 | numeric | 23 | 10 | √ | 0.0000000000 | 匹配数量 |
| 3 | fsupplytype | 供应类型来源 | varchar | 50 |  | √ | ' ' | 供应类型来源,枚举: A :库存 B :生产工单 C :日生产计划 D :尾单 E :配额 F :缺配额组织 |
| 4 | fmatchseq | 匹配序号 | int8 | 64 |  | √ | 0 | 匹配序号 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbillflag | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsupplytime | 供应时间 | timestamp | 0 |  |  | null | 供应时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_dpsallocentry |  | fid,fseq |
| 2 | pk_t_mds_dpsallocentry |  | fentryid |
