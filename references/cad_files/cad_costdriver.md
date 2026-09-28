# 费用分配标准-cad_costdriver

## 费用分配标准-使用范围位图表 t_cad_costdriver_m

- **表名称：** 费用分配标准-使用范围位图表
- **表名：** t_cad_costdriver_m

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
| 1 | pk_t_cad_costdriver_m |  | forgid |

---

## 费用分配标准-多语言表 t_cad_costdriver_l

- **表名称：** 费用分配标准-多语言表
- **表名：** t_cad_costdriver_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costdriver_l |  | fid,flocaleid |
| 2 | t_cad_costdriver_l_pkey |  | fpkid |

---

## 费用分配标准-使用范围表 t_cad_costdriver_u

- **表名称：** 费用分配标准-使用范围表
- **表名：** t_cad_costdriver_u

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
| 1 | idx_t_cad_costdriver_u_uo |  | fuseorgid |
| 2 | t_cad_costdriver_u_pkey |  | fdataid,fuseorgid |

---

## 费用分配标准-主表 t_cad_costdriver

- **表名称：** 费用分配标准-主表
- **表名：** t_cad_costdriver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatchpattern | 匹配模式 | varchar | 30 |  | √ | 'resource' | 匹配模式,枚举: resource :资源 resourcetype :资源类型 |
| 3 | fapplication | fapplication | varchar | 30 |  | √ | ' ' |  |
| 4 | fsubelementid | fsubelementid | int8 | 64 |  | √ | 0 |  |
| 5 | fworkactivityid | 作业活动 | int8 | 64 |  | √ | 0 | 作业活动 cad_new_workactivity |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 8 | fislinkresource | 关联资源 | bpchar | 1 |  | √ | '0' | 关联资源 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fformulastr | 公式设置 | varchar | 2000 |  | √ | ' ' | 公式设置 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fformula | 公式设置 | varchar | 2000 |  | √ | ' ' | 公式设置 |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 26 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fallocclass | 分配层级 | varchar | 30 |  | √ | ' ' | 分配层级,枚举: COSTCENTER :成本中心 MATERIAL :物料 COSTOBJECT :成本核算对象 MATERIALGROUP :物料分类 |
| 28 | fresourcetype | 资源类型 | varchar | 30 |  | √ | ' ' | 资源类型,枚举: A :设备资源 B :工具资源 C :工装资源 D :模具资源 E :制造人员 |
| 29 | fiscomplexcd | 复合分配标准 | bpchar | 1 |  | √ | '0' | 复合分配标准 |
| 30 | fmatchreport | 匹配资源耗用量归集单 | varchar | 30 |  | √ | 'total' | 匹配资源耗用量归集单,枚举: total :实际工时 much :实际用量 |
| 31 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 32 | fenable | 使用状态 | varchar | 30 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 34 | fisrelatedwork | 关联作业 | bpchar | 1 |  | √ | '0' | 关联作业 |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costdriver |  | fmasterid |
| 2 | t_cad_costdriver_pkey |  | fid |
| 3 | idx_t_cad_costdriver_master |  | fmasterid |
| 4 | idx_t_cad_costdriver_createorg |  | fcreateorgid |

---

## 资源-多选基础资料表 t_cad_costdriver_resource

- **表名称：** 资源-多选基础资料表
- **表名：** t_cad_costdriver_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costdriver_resource |  | fpkid |
