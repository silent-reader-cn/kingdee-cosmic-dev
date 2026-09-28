# 产品组-sco_productweight

## 联产品信息分录-子表 t_sco_productweightentry

- **表名称：** 联产品信息分录-子表
- **表名：** t_sco_productweightentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0 | 分配权重 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fjointproductmasterid | 联产品物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fjointproductid | 联产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_productweightentry |  | fentryid |
| 2 | idx_sco_productweightentry |  | fid |
| 3 | idx_sco_productweightentry_j |  | fjointproductid |

---

## 产品组-多语言表 t_sco_productweight_l

- **表名称：** 产品组-多语言表
- **表名：** t_sco_productweight_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_productweight_l |  | fpkid |

---

## 产品组-主表 t_sco_productweight

- **表名称：** 产品组-主表
- **表名：** t_sco_productweight

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fproductweight | 分配权重 | numeric | 23 | 10 | √ | 0 | 分配权重 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fexpdate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | fproductmasterid | 主产品物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | feffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fproductid | 主产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: 1 :自动生成-标准成本 2 :自动生成-数量 3 :手工新增 |
| 21 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_productweight |  | fid |
| 2 | idx_sco_productweight_product |  | fproductid |
| 3 | idx_sco_productweight_number |  | fnumber |
