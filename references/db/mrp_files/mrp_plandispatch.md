# 计划调度方案-mrp_plandispatch

## 计划调度方案-多语言表 t_mrp_plandispatch_l

- **表名称：** 计划调度方案-多语言表
- **表名：** t_mrp_plandispatch_l

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
| 1 | idx_mrp_plandispatch_l |  | fid,flocaleid |
| 2 | pk_t_mrp_plandispatch_l |  | fpkid |

---

## 计划调度方案-分表 t_mrp_plandispatch_e

- **表名称：** 计划调度方案-分表
- **表名：** t_mrp_plandispatch_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataversionid | 数据版本 | int8 | 64 |  | √ | 0 | [数据版本 msplan_ds_version](../msplan_files/msplan_ds_version.md) |
| 3 | fisexecute | 是否顺序执行 | bpchar | 1 |  | √ | '0' | 是否顺序执行 |
| 4 | fforecastplanlogno | 预测计划日志编码 | varchar | 255 |  | √ | ' ' | 预测计划日志编码 |
| 5 | fforecastplanlog | 预测计划日志 | varchar | 255 |  | √ | ' ' | 预测计划日志 |
| 6 | fisrunning | 立即同步 | bpchar | 1 |  | √ | '0' | 立即同步 |
| 7 | fforecastplanno | 预测计划方案编码 | varchar | 255 |  | √ | ' ' | 预测计划方案编码 |
| 8 | fdataversionlog | 数据版本日志 | varchar | 50 |  | √ | ' ' | 数据版本日志 |
| 9 | fforecastplanname | 预测计划方案名称 | varchar | 255 |  | √ | ' ' | 预测计划方案名称 |
| 10 | fforecastplanstatus | 预测计划运行状态 | varchar | 255 |  | √ | ' ' | 预测计划运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |
| 11 | fforecastplanrunid | 预测计划方案ID | varchar | 255 |  | √ | ' ' | 预测计划方案ID |
| 12 | fdataversionstatus | 同步设置运行状态 | varchar | 30 |  | √ | ' ' | 同步设置运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_plandispatch_e |  | fforecastplanno |
| 2 | pk_t_mrp_plandispatch_e |  | fid |

---

## 计划调度方案-主表 t_mrp_plandispatch

- **表名称：** 计划调度方案-主表
- **表名：** t_mrp_plandispatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdpsname | 供应组织分配方案名称 | varchar | 255 |  | √ | ' ' | 供应组织分配方案名称 |
| 3 | frepeat | 重复运算 | bpchar | 1 |  | √ | ' ' | 重复运算 |
| 4 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 5 | fisrelease | 已发布 | bpchar | 1 |  | √ | '0' | 已发布 |
| 6 | freqplanid | 需求方案id | varchar | 2000 |  | √ | ' ' | 需求方案id |
| 7 | frunningtype | 运行时间类型 | varchar | 30 |  | √ | ' ' | 运行时间类型,枚举: 0 :立即运算 1 :预约时间运算 |
| 8 | fmrpexp | 异常信息 | varchar | 2000 |  | √ | ' ' | 异常信息 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | freqplanrunstatus | 需求计划运行状态 | bpchar | 1 |  | √ | ' ' | 需求计划运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |
| 11 | fplanid | 计划号 | varchar | 255 |  | √ | ' ' | 计划号 |
| 12 | fforecastname | 预测冲减运算名称 | varchar | 255 |  | √ | ' ' | 预测冲减运算名称 |
| 13 | fdaysofmon | 月 | varchar | 255 |  | √ | ' ' | 月 |
| 14 | freqplanname | 需求方案名称 | varchar | 2000 |  | √ | ' ' | 需求方案名称 |
| 15 | fmrplog1 | MRP计划运算号 | varchar | 50 |  | √ | ' ' | MRP计划运算号 |
| 16 | fplangramid | 计划方案 | int8 | 64 |  | √ | 0 | [计划方案 mrp_planscheme](../msplan_files/mrp_planscheme.md) |
| 17 | fforecastrunstatus | 预测冲减运行状态 | bpchar | 1 |  | √ | ' ' | 预测冲减运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |
| 18 | fdspnumber | 供应组织分配方案编码 | varchar | 255 |  | √ | ' ' | 供应组织分配方案编码 |
| 19 | fforecastids | 预测冲减运算ID | varchar | 1000 |  | √ | ' ' | 预测冲减运算ID |
| 20 | fdaysofweek | 周 | varchar | 255 |  | √ | ' ' | 周 |
| 21 | fdsplog | 供应组织分配运算日志 | varchar | 255 |  | √ | ' ' | 供应组织分配运算日志 |
| 22 | fplanorgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fforecastlogid | 预测冲减日志id | int8 | 64 |  | √ | 0 | 预测冲减日志id |
| 24 | freqplanlog1 | 需求计划运算日志 | varchar | 2000 |  | √ | ' ' | 需求计划运算日志 |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 27 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 28 | fforecastno | 预测冲减运算编码 | varchar | 2000 |  | √ | ' ' | 预测冲减运算编码 |
| 29 | freqplanlog | freqplanlog | int8 | 64 |  | √ | 0 |  |
| 30 | fisallowdateinpast | 允许计划订单开始日期在过去 | bpchar | 1 |  | √ | '0' | 允许计划订单开始日期在过去 |
| 31 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 34 | fisllc | 重算低位码 | bpchar | 1 |  | √ | '0' | 重算低位码 |
| 35 | fforecastorgid | fforecastorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fplan | cron表达式 | varchar | 255 |  | √ | ' ' | cron表达式 |
| 37 | fdpsrunstatus | 供应组织分配运行状态 | varchar | 255 |  | √ | ' ' | 供应组织分配运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | fjobid | 作业号 | varchar | 255 |  | √ | ' ' | 作业号 |
| 41 | fmrplog | fmrplog | int8 | 64 |  | √ | 0 |  |
| 42 | fforecastlog | fforecastlog | varchar | 255 |  | √ | ' ' |  |
| 43 | frepeattype | 时间重复类型 | varchar | 30 |  | √ | ' ' | 时间重复类型,枚举: 0 :周 1 :月 2 :自定义 |
| 44 | fforecastlognumber | 预测冲减日志 | varchar | 255 |  | √ | ' ' | 预测冲减日志 |
| 45 | freqplannumber | 需求方案编码 | varchar | 2000 |  | √ | ' ' | 需求方案编码 |
| 46 | frunstatus | 运行状态 | bpchar | 1 |  | √ | ' ' | 运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |
| 47 | fbizplanid | 业务方案配置 | int8 | 64 |  | √ | 0 | [业务方案配置 mrp_businessplan](../msplan_files/mrp_businessplan.md) |
| 48 | fmrprunstatus | 运行状态 | bpchar | 1 |  | √ | ' ' | 运行状态,枚举: A :运行中 B :异常终止 C :正常结束 D :手工终止 |
| 49 | fisbomcheck | BOM嵌套检查 | bpchar | 1 |  | √ | '0' | BOM嵌套检查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_plandispatch |  | fid |
| 2 | idx_mrp_plandispatch |  | fnumber |
