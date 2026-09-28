# 累计积分记录-er_integralrecord

## 累计积分记录-使用范围位图表 t_er_integralrecord_m

- **表名称：** 累计积分记录-使用范围位图表
- **表名：** t_er_integralrecord_m

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
| 1 | pk_t_er_integralrecord_m |  | forgid |

---

## 单据体-子表 t_er_integralrecordentry

- **表名称：** 单据体-子表
- **表名：** t_er_integralrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fexpenseamount | 本位币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本位币金额 |
| 4 | fexpenseitemicon | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fscore | fscore | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_inreen_fseq |  | fid,fseq |
| 2 | t_er_integralrecordentry_pkey |  | fentryid |

---

## 累计积分记录-多语言表 t_er_integralrecord_l

- **表名称：** 累计积分记录-多语言表
- **表名：** t_er_integralrecord_l

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
| 1 | idx_t_er_integralrecord_l_lid |  | fid,flocaleid |
| 2 | t_er_integralrecord_l_pkey |  | fpkid |

---

## 累计积分记录-使用范围表 t_er_integralrecord_u

- **表名称：** 累计积分记录-使用范围表
- **表名：** t_er_integralrecord_u

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
| 1 | idx_t_er_integralrecord_u_uo |  | fuseorgid |
| 2 | t_er_integralrecord_u_pkey |  | fdataid,fuseorgid |

---

## 累计积分记录-主表 t_er_integralrecord

- **表名称：** 累计积分记录-主表
- **表名：** t_er_integralrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhappendate | 积分发生日期 | timestamp | 0 |  |  | null | 积分发生日期 |
| 3 | ftotalamount | 订单总价格 | numeric | 23 | 10 | √ | 0.0000000000 | 订单总价格 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fisparttime | 参与定时任务 | bpchar | 1 |  | √ | '0' | 参与定时任务 |
| 8 | fdaycount | 天数 | int8 | 64 |  | √ | 0 | 天数 |
| 9 | fitemicon | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 36 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fticketprice | 机票价格 | numeric | 23 | 10 | √ | 0.0000000000 | 机票价格 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fintegralid | 积分人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 22 | fintegralscore | 积分分数 | numeric | 23 | 10 | √ | 0.0000000000 | 积分分数 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fintegraltype | 积分类型 | bpchar | 1 |  | √ | ' ' | 积分类型,枚举: 1 :点赞 2 :折扣航班 3 :酒店积分 4 :首次登陆 |
| 25 | fisvital | 活力积分 | bpchar | 1 |  | √ | '0' | 活力积分 |
| 26 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fexpenseamount | fexpenseamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fstandprice | 全价机票 | numeric | 23 | 10 | √ | 0.0000000000 | 全价机票 |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_integralrecord_pkey |  | fid |
| 2 | idx_er_ir_fintegralid |  | fintegralid |
| 3 | idx_t_er_integralrecord_master |  | fmasterid |
| 4 | idx_t_er_integralrecord_createorg |  | fcreateorgid |
