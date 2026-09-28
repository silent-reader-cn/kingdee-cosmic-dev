# 产品组-sco_productintogroup

## 联产品分配权重明细分录-子表 t_sco_productgroup_detail

- **表名称：** 联产品分配权重明细分录-子表
- **表名：** t_sco_productgroup_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubelementid | 成本子要素编码 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 2 | fallocweight | 分配权重 | int8 | 64 |  | √ | 0 | 分配权重 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
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
| 1 | pk_sco_productgroup_detail |  | fdetailid |
| 2 | idx_sco_productgroup_detail |  | felementid,fsubelementid |

---

## 产品信息分录-子表 t_sco_productgroupentry

- **表名称：** 产品信息分录-子表
- **表名：** t_sco_productgroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 3 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0 | 分配权重 |
| 4 | fgroupcategoryid | 分组类型 | int8 | 64 |  | √ | 0 | 辅助属性定义 bd_auxproperty |
| 5 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 10 | fstocktype | 入库类型 | varchar | 30 |  | √ | ' ' | 入库类型,枚举: 1 :合格品 2 :不合格品 3 :待检品 4 :报废品 |
| 11 | falloctype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :成本核算对象指定 2 :手工指定 3 :定额 |
| 12 | fimporttype | 引入类型 | varchar | 1 |  | √ | ' ' | 引入类型,枚举: p :产品组引入 w :联副产品引入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_productgroupentry |  | fentryid |
| 2 | idx_sco_productgroupentry |  | fid,fseq |

---

## 产品组-多语言表 t_sco_productintogroup_l

- **表名称：** 产品组-多语言表
- **表名：** t_sco_productintogroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_productintogroup_l |  | fid,flocaleid,fname |
| 2 | pk_sco_productintogroup_l |  | fpkid |

---

## 产品组-主表 t_sco_productintogroup

- **表名称：** 产品组-主表
- **表名：** t_sco_productintogroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | funauditflag | 反审核标识 | varchar | 10 |  | √ | ' ' | 反审核标识,枚举: |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsrcfield | 源单字段 | varchar | 50 |  | √ | ' ' | 源单字段 |
| 7 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: MANUAL :手工新增 SYS :系统生成 |
| 8 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fimporttype | fimporttype | varchar | 1 |  | √ | ' ' |  |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fcalorgid | 核算组织(废弃-240324多核算体系改造) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fgroupfield | 分组字段 | varchar | 80 |  | √ | ' ' | 分组字段,枚举: bd_auxproperty :辅助属性 bd_invtype :库存类型 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 26 | fgrouptype | 分组依据 | varchar | 30 |  | √ | ' ' | 分组依据,枚举: 1 :主联副 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_productintogroup_ct |  | fcreateorgid |
| 2 | pk_sco_productintogroup |  | fid |
| 3 | idk_sco_productintogroup |  | fcreatetime,forgid |
| 4 | idx_sco_productintogroup_mt |  | fmasterid |
| 5 | idx_t_sco_productintogroup_master |  | fmasterid |
| 6 | idx_t_sco_productintogroup_createorg |  | fcreateorgid |

---

## 产品组-使用范围表 t_sco_productintogroup_u

- **表名称：** 产品组-使用范围表
- **表名：** t_sco_productintogroup_u

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
| 1 | pk_t_sco_productintogroup_u |  | fdataid,fuseorgid |
| 2 | idx_t_sco_productintogroup_u_uo |  | fuseorgid |
