# 预算MRP业务流方案-xkbm_mrpbizscheme

## 输入项转换规则-子表 t_xkbm_mrpinrule

- **表名称：** 输入项转换规则-子表
- **表名：** t_xkbm_mrpinrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbillinfieldkey | 预算需求计划单字段标识 | varchar | 255 |  | √ | ' ' | 预算需求计划单字段标识 |
| 2 | fbillinfieldtype | 预算需求计划单 | varchar | 10 |  | √ | ' ' | 预算需求计划单,枚举: 0 :需求组织 1 :供应组织 2 :物料 3 :需求数量 4 :需求日期 5 :项目 6 :任务 |
| 3 | frptschemeinfieldkey | 对应模板样式方案字段标识 | varchar | 2000 |  | √ | ' ' | 对应模板样式方案字段标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillinfullfieldkey | 预算需求计划单字段完整标识 | varchar | 500 |  | √ | ' ' | 预算需求计划单字段完整标识 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fmulirptschemeinfieldname | 对应模板样式方案多语言 | varchar | 2000 |  | √ | ' ' | 对应模板样式方案多语言 |
| 9 | fmulibillinfieldname | 预算需求计划单多语言 | varchar | 570 |  | √ | ' ' | 预算需求计划单多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_mrpinrule |  | fdetailid |
| 2 | idx_xkbm_mrpinrule_fentryid |  | fentryid |

---

## 预算MRP业务流方案-主表 t_xkbm_mrpbizscheme

- **表名称：** 预算MRP业务流方案-主表
- **表名：** t_xkbm_mrpbizscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fname | 名称 | varchar | 570 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算MRP业务流方案分组 xkbm_mrpbizschemegroup](../xkbm_files/xkbm_mrpbizschemegroup.md) |
| 6 | fenableid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fincludeproject | 考虑项目 | bpchar | 1 |  | √ | ' ' | 考虑项目 |
| 9 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 10 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 11 | fincludeauxpty | 考虑物料的辅助属性 | bpchar | 1 |  | √ | ' ' | 考虑物料的辅助属性 |
| 12 | fcoverunauditreport | 覆盖已创建未审核的预算表 | bpchar | 1 |  | √ | ' ' | 覆盖已创建未审核的预算表 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fautocreateplanbill | 预算表审核时，自动生成预算需求计划单 | bpchar | 1 |  | √ | ' ' | 预算表审核时，自动生成预算需求计划单 |
| 15 | fcycles | 包含周期 | varchar | 50 |  | √ | ' ' | 包含周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 16 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fscheme | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 20 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fcycle | 周期类型 | varchar | 10 |  | √ | ' ' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fincludetask | 考虑任务 | bpchar | 1 |  | √ | ' ' | 考虑任务 |
| 24 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpbizscheme |  | fscheme,fcycle,fcycles |
| 2 | pk_xkbm_mrpbizscheme |  | fid |

---

## 预算MRP业务流方案-多语言表 t_xkbm_mrpbizscheme_l

- **表名称：** 预算MRP业务流方案-多语言表
- **表名：** t_xkbm_mrpbizscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 570 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpbizscheme_l |  | fid,flocaleid |
| 2 | pk_xkbm_mrpbizscheme_l |  | fpkid |

---

## 输出项转换规则-多语言表 t_xkbm_mrpoutrule_l

- **表名称：** 输出项转换规则-多语言表
- **表名：** t_xkbm_mrpoutrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmuliconditionnameout | 过滤条件多语言 | varchar | 570 |  | √ | ' ' | 过滤条件多语言 |
| 2 | fmulirptschemeoutname | 对应模板样式方案多语言 | varchar | 2000 |  | √ | ' ' | 对应模板样式方案多语言 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fmulibilloutfieldname | 预算计划订单多语言 | varchar | 570 |  | √ | ' ' | 预算计划订单多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpoutrule_l |  | fdetailid,flocaleid |
| 2 | pk_xkbm_mrpoutrule_l |  | fpkid |

---

## 预算MRP运算输出项-多语言表 t_xkbm_mrpbizschemeout_l

- **表名称：** 预算MRP运算输出项-多语言表
- **表名：** t_xkbm_mrpbizschemeout_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdescriptionout |  | varchar | 50 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_mrpbizschemeout_l |  | fpkid |
| 2 | idx_xkbm_mrpbizschemeout_l |  | fentryid,flocaleid |

---

## 输入项转换规则-多语言表 t_xkbm_mrpinrule_l

- **表名称：** 输入项转换规则-多语言表
- **表名：** t_xkbm_mrpinrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fmulirptschemeinfieldname | 对应模板样式方案多语言 | varchar | 2000 |  | √ | ' ' | 对应模板样式方案多语言 |
| 5 | fmulibillinfieldname | 预算需求计划单多语言 | varchar | 570 |  | √ | ' ' | 预算需求计划单多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpinrule_l |  | fdetailid,flocaleid |
| 2 | pk_xkbm_mrpinrule_l |  | fpkid |

---

## 输出项转换规则-子表 t_xkbm_mrpoutrule

- **表名称：** 输出项转换规则-子表
- **表名：** t_xkbm_mrpoutrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbilloutfullfieldkey | 预算计划订单字段完整标识 | varchar | 500 |  | √ | ' ' | 预算计划订单字段完整标识 |
| 2 | fconditionjsonout | 过滤条件json | varchar | 2000 |  | √ | ' ' | 过滤条件json |
| 3 | fbilloutfieldtype | 预算计划订单 | varchar | 10 |  | √ | ' ' | 预算计划订单,枚举: 0 :日期 1 :供应组织 2 :物料 3 :项目 4 :任务 5 :数量 |
| 4 | fmuliconditionnameout | 过滤条件多语言 | varchar | 570 |  | √ | ' ' | 过滤条件多语言 |
| 5 | fmulirptschemeoutname | 对应模板样式方案多语言 | varchar | 2000 |  | √ | ' ' | 对应模板样式方案多语言 |
| 6 | fconditionsqlout | 过滤条件sql | varchar | 2000 |  | √ | ' ' | 过滤条件sql |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fbilloutfieldkey | 预算计划订单字段标识 | varchar | 255 |  | √ | ' ' | 预算计划订单字段标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | frptschemeoutfieldkey | 对应模板样式方案字段标识 | varchar | 2000 |  | √ | ' ' | 对应模板样式方案字段标识 |
| 12 | fmulibilloutfieldname | 预算计划订单多语言 | varchar | 570 |  | √ | ' ' | 预算计划订单多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpoutrule_fentryid |  | fentryid |
| 2 | pk_xkbm_mrpoutrule |  | fdetailid |

---

## 预算MRP运算输出项-子表 t_xkbm_mrpbizschemeout

- **表名称：** 预算MRP运算输出项-子表
- **表名：** t_xkbm_mrpbizschemeout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frptschemeout |  | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 3 | fdescriptionout |  | varchar | 50 |  | √ | ' ' |  |
| 4 | fbusinesstypeout |  | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpbizschemeout_fid |  | fid |
| 2 | pk_xkbm_mrpbizschemeout |  | fentryid |

---

## 预算MRP运算输入项-子表 t_xkbm_mrpbizschemein

- **表名称：** 预算MRP运算输入项-子表
- **表名：** t_xkbm_mrpbizschemein

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinesstypein |  | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 3 | frptschemein |  | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdescriptionin |  | varchar | 50 |  | √ | ' ' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpbizschemein_fid |  | fid |
| 2 | pk_xkbm_mrpbizschemein |  | fentryid |

---

## 预算MRP运算输入项-多语言表 t_xkbm_mrpbizschemein_l

- **表名称：** 预算MRP运算输入项-多语言表
- **表名：** t_xkbm_mrpbizschemein_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdescriptionin |  | varchar | 50 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_mrpbizschemein_l |  | fentryid,flocaleid |
| 2 | pk_xkbm_mrpbizschemein_l |  | fpkid |
