# 共耗材料分配标准-sco_matallocstd

## 共耗材料分配标准-主表 t_sco_matallocstd

- **表名称：** 共耗材料分配标准-主表
- **表名：** t_sco_matallocstd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frepetitionrow | 重复行数 | int8 | 64 |  | √ | 0 | 重复行数 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsourceid | 源单id(复制的单据id) | int8 | 64 |  | √ | 0 | 源单id(复制的单据id) |
| 9 | fexpdate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本核算 aca :实际成本核算 eca :服务成本核算 |
| 12 | feffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_matallocstd |  | fid |
| 2 | index_sco_matallocstd |  | forgid |

---

## 分配标准-子表 t_sco_matallocstdentry

- **表名称：** 分配标准-子表
- **表名：** t_sco_matallocstdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 4 | fallocdim | 分配维度 | varchar | 255 |  | √ | ' ' | 分配维度,枚举: configuredcode :配置号 tracknumber :跟踪号 project :项目号 lot :批号 |
| 5 | fproductgroupid | 产品组编码 | int8 | 64 |  | √ | 0 | [产品组 cad_productintogroup](../aca_files/cad_productintogroup.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fmaterialgroupid | 物料分类编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | fcostdriverid | 分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_matallocstdentry |  | fentryid |
| 2 | idx_sco_matallocstdentry |  | fid |

---

## 产品明细-子表 t_sco_productsubentry

- **表名称：** 产品明细-子表
- **表名：** t_sco_productsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_productsubentry |  | fdetailid |
| 2 | index_sco_productsubentry |  | fentryid,fmaterialid |
