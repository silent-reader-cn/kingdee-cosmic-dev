# 预测\需求计划关联关系-mds_corl

## 来源单据体-子表 t_mds_fccorlentry

- **表名称：** 来源单据体-子表
- **表名：** t_mds_fccorlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | fentrymodifier | int8 | 64 |  | √ | 0 |  |
| 3 | fvrntype | 版本类别 | varchar | 30 |  | √ | ' ' | 版本类别,枚举: 0 :预测 1 :需求计划 |
| 4 | fentrycreatedate | fentrycreatedate | timestamp | 0 |  |  | null |  |
| 5 | fpropt | 百分率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 百分率(%) |
| 6 | fsrcvrnnum | 版本编码 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fentrycreator | fentrycreator | int8 | 64 |  | √ | 0 |  |
| 10 | fentrymodifydate | fentrymodifydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fccorlentry |  | fid,fseq |
| 2 | t_mds_fccorlentry_pkey |  | fentryid |

---

## 预测\需求计划关联关系-主表 t_mds_fccorl

- **表名称：** 预测\需求计划关联关系-主表
- **表名：** t_mds_fccorl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftgtvrnnum | 目标版本编码 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fcorlremark | 关联关系备注 | varchar | 255 |  | √ | ' ' | 关联关系备注 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 关联关系编码 | varchar | 30 |  | √ | ' ' | 关联关系编码 |
| 21 | fcorltype | 关联关系类型 | varchar | 30 |  | √ | ' ' | 关联关系类型,枚举: Forecast :预测 MDS :需求计划 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fccorl |  | fnumber,fcreateorgid |
| 2 | t_mds_fccorl_pkey |  | fid |
| 3 | idx_t_mds_fccorl_createorg |  | fcreateorgid |
| 4 | idx_t_mds_fccorl_master |  | fmasterid |

---

## 预测\需求计划关联关系-使用范围表 t_mds_fccorl_u

- **表名称：** 预测\需求计划关联关系-使用范围表
- **表名：** t_mds_fccorl_u

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
| 1 | idx_t_mds_fccorl_u_uo |  | fuseorgid |
| 2 | t_mds_fccorl_u_pkey |  | fdataid,fuseorgid |

---

## 预测\需求计划关联关系-使用范围位图表 t_mds_fccorl_m

- **表名称：** 预测\需求计划关联关系-使用范围位图表
- **表名：** t_mds_fccorl_m

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
| 1 | pk_t_mds_fccorl_m |  | forgid |

---

## 预测\需求计划关联关系-多语言表 t_mds_fccorl_l

- **表名称：** 预测\需求计划关联关系-多语言表
- **表名：** t_mds_fccorl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 关联关系名称 | varchar | 100 |  | √ | ' ' | 关联关系名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_fccorl_l |  | fid,flocaleid |
| 2 | t_mds_fccorl_l_pkey |  | fpkid |
