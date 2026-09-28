# 出入库序列配置-cal_queuesetting

## 出入库序列配置-主表 t_cal_queuesetting

- **表名称：** 出入库序列配置-主表
- **表名：** t_cal_queuesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbizpluginid | 插件 | int8 | 64 |  | √ | 0 | 核算预置插件 cal_plugin |
| 5 | ffilterstr_tag | filterstr_详情 | text | 0 |  |  | null | filterstr_详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fqueuetype | 序列方向 | varchar | 5 |  | √ | ' ' | 序列方向,枚举: A :入库序列 B :出库序列 |
| 9 | ffilterstr | filterstr | varchar | 255 |  |  | null | filterstr |
| 10 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 状态 | varchar | 5 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 15 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fbilltypeid | 单据类型 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_queuesetting_pkey |  | fid |
| 2 | idx_cal_queueset_calorg |  | fcalorgid |
