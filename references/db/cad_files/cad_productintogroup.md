# 产品组-cad_productintogroup

## 产品组-使用范围位图表 t_aca_productintogroup_m

- **表名称：** 产品组-使用范围位图表
- **表名：** t_aca_productintogroup_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_productintogroup_m |  | forgid |

---

## 产品组-多语言表 t_aca_productintogroup_l

- **表名称：** 产品组-多语言表
- **表名：** t_aca_productintogroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | 'zh_CN' | localeid |
| 4 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aca_productintogroup_l |  | fpkid |
| 2 | idx_aca_productintogroup_l |  | fid,flocaleid,fname |

---

## 产品组-使用范围表 t_aca_productintogroup_u

- **表名称：** 产品组-使用范围表
- **表名：** t_aca_productintogroup_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_productintogroup_u |  | fdataid,fuseorgid |
| 2 | idx_t_aca_productintogroup_u_uo |  | fuseorgid |

---

## 产品信息分录-子表 t_aca_productgroupentry

- **表名称：** 产品信息分录-子表
- **表名：** t_aca_productgroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 6 | fstocktype | 入库类型 | varchar | 30 |  | √ | ' ' | 入库类型,枚举: 1 :合格品 2 :不合格品 3 :待检品 4 :报废品 |
| 7 | falloctype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :成本核算对象指定 2 :手工指定 3 :定额 |
| 8 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 9 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0.0000000000 | 分配权重 |
| 10 | fgroupcategoryid | fgroupcategoryid | int8 | 64 |  | √ | 0 |  |
| 11 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | finvstatus | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 14 | fimporttype | 引入类型 | varchar | 1 |  | √ | ' ' | 引入类型,枚举: p :产品组引入 w :联副产品引入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_productgroupentry |  | fid,fseq |
| 2 | idx_progroupen_mat |  | fmaterialid |
| 3 | pk_t_aca_productgroupentry |  | fentryid |

---

## 产品组-主表 t_aca_productintogroup

- **表名称：** 产品组-主表
- **表名：** t_aca_productintogroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | funauditflag | 反审核标识 | varchar | 1 |  | √ | ' ' | 反审核标识,枚举: |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrcfield | 源单字段 | varchar | 50 |  | √ | ' ' | 源单字段 |
| 7 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: MANUAL :手工新增 SYS :系统生成 |
| 8 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | '0' | 成本主体 cal_bd_costaccount |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcalorgid | 核算组织(废弃-230629多核算体系改造) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fgroupfield | 分组字段 | varchar | 60 |  | √ | ' ' | 分组字段,枚举: 1 :库存状态 2 :辅助属性 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fgrouptype | 分组依据 | varchar | 30 |  | √ | ' ' | 分组依据,枚举: 1 :主联副 2 :等级 3 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_aca_productintogroup_master |  | fmasterid |
| 2 | pk_t_aca_productintogroup |  | fid |
| 3 | idk_aca_productintogroup |  | fcreatetime,forgid |
| 4 | idx_t_aca_productintogroup_createorg |  | fcreateorgid |
| 5 | idx_progroup_org |  | fcalorgid |

---

## 联产品分配权重明细分录-子表 t_aca_productgroup_detail

- **表名称：** 联产品分配权重明细分录-子表
- **表名：** t_aca_productgroup_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fallocweight | 分配权重 | numeric | 23 | 10 |  | 0 | 分配权重 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | felementid | 成本要素编码 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_progroupde_sube |  | fsubelementid |
| 2 | idx_t_aca_productgroup_detail |  | felementid,fsubelementid |
| 3 | idx_aca_productgroupd_fentryid |  | fentryid |
| 4 | pk_t_aca_productgroup_detail |  | fdetailid |
