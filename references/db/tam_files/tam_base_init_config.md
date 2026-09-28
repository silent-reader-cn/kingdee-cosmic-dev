# 基础初始化配置-tam_base_init_config

## 基础初始化配置-主表 t_tam_base_init_config

- **表名称：** 基础初始化配置-主表
- **表名：** t_tam_base_init_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fistaxmaincomplete | 纳税主体信息 | varchar | 50 |  | √ | ' ' | 纳税主体信息,枚举: 0 :未完成 1 :已完成 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fpagestatus | 任务进度 | varchar | 50 |  | √ | ' ' | 任务进度 |
| 9 | fisorgmappingcomplete | 税务组织映射关系 | varchar | 50 |  | √ | ' ' | 税务组织映射关系,枚举: 0 :未完成 1 :已完成 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fisorgcomplete | 税务组织信息 | varchar | 50 |  | √ | ' ' | 税务组织信息,枚举: 0 :未完成 1 :已完成 |
| 13 | fisorgparamcomplete | 税务参数配置 | varchar | 50 |  | √ | ' ' | 税务参数配置,枚举: 0 :未完成 1 :已完成 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fisorggroupcomplete | 汇总方案 | varchar | 50 |  | √ | ' ' | 汇总方案,枚举: 0 :未完成 1 :已完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tam_base_init_config_1 |  | forgid |
| 2 | pk_tam_base_init_config |  | fid |
