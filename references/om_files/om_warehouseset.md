# 委外仓库设置-om_warehouseset

## 委外仓库设置-主表 t_om_warehouseset

- **表名称：** 委外仓库设置-主表
- **表名：** t_om_warehouseset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forgfield | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finwarehouse | 调入仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | finorg | 调入组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcodingobj | fcodingobj | varchar | 50 |  | √ | ' ' |  |
| 10 | ffilterruler | ffilterruler | varchar | 255 |  | √ | ' ' |  |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: C :已审核 |
| 12 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ffilterruler_tag | ffilterruler_tag | text | 0 |  |  | null |  |
| 16 | finlocation | 调入仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_om_warehouseset |  | fid |
| 2 | idx_om_warehouseset |  | forgfield,finorg,fsupplier |

---

## 委外仓库设置-多语言表 t_om_warehouseset_l

- **表名称：** 委外仓库设置-多语言表
- **表名：** t_om_warehouseset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_warehouseset_l |  | fpkid |
| 2 | idx_om_warehouseset_l |  | fid,flocaleid |
