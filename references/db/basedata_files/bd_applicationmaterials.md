# 物料批量申请单-bd_applicationmaterials

## 申请单物料明细-多语言表 t_bd_appmaterialsentry_l

- **表名称：** 申请单物料明细-多语言表
- **表名：** t_bd_appmaterialsentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fmaterialname | 申请物料名称 | varchar | 255 |  | √ | ' ' | 申请物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_appmaterialsentry_l_pkey |  | fpkid |
| 2 | idx_bd_appmaterialsentry_l_bil |  | fentryid,flocaleid |

---

## 物料批量申请单-主表 t_bd_appmaterials

- **表名称：** 物料批量申请单-主表
- **表名：** t_bd_appmaterials

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 8 | fproposer | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 模板物料管控策略 | varchar | 5 |  | √ | ' ' | 模板物料管控策略,枚举: 2 :自由分配 5 :全局共享 7 :私有 |
| 11 | fcreateorg | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ffilingdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbilltype | 单据类型 | varchar | 5 |  | √ | ' ' | 单据类型,枚举: 1 :备件类物料申请单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_appmaterials_pkey |  | fid |
| 2 | idx_bd_appmaterials_forfbizfno |  | forgid,fbillno,ffilingdate |

---

## 申请单物料明细-子表 t_bd_appmaterialsentry

- **表名称：** 申请单物料明细-子表
- **表名：** t_bd_appmaterialsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodel | fmodel | varchar | 255 |  | √ | ' ' |  |
| 3 | fgroup | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 4 | fformalmaterialnumber | 正式物料编码 | varchar | 80 |  | √ | ' ' | 正式物料编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fistempmaterial | 是否模板物料 | bpchar | 1 |  | √ | '0' | 是否模板物料 |
| 7 | fapplynumber | 申请物料编码 | varchar | 80 |  | √ | ' ' | 申请物料编码 |
| 8 | ftemplatematerial | 模板物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 12 | fmaterialtype | 物料类型 | varchar | 5 |  | √ | ' ' | 物料类型,枚举: 1 :物资 7 :费用 8 :资产 9 :服务 3 :套件 2 :虚拟件 4 :可配置件 5 :特征件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_appmaterialsentry_pkey |  | fentryid |
| 2 | idx_bd_appmaterialsentry_billi |  | fid |

---

## 物料批量申请单-多语言表 t_bd_appmaterials_l

- **表名称：** 物料批量申请单-多语言表
- **表名：** t_bd_appmaterials_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_appmaterials_l_pkey |  | fpkid |
| 2 | idx_t_bd_appmaterials_l_fid |  | fid,flocaleid |
