# 坏账计提（废弃）-ar_baddebtresult

## 坏账计提（废弃）-主表 t_ar_baddebtresult

- **表名称：** 坏账计提（废弃）-主表
- **表名：** t_ar_baddebtresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisfirst | 是否第一期间 | bpchar | 1 |  | √ | '0' | 是否第一期间 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fbillstatus | 计提状态 | varchar | 5 |  | √ | ' ' | 计提状态,枚举: A :未计提 B :已计提 |
| 7 | fpolicytypeid | 政策类型 | int8 | 64 |  | √ | 0 | 政策类型 ar_policytype |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpolicyid | 应收政策ID | int8 | 64 |  | √ | 0 | 应收政策ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_baddebtresult_org |  | forgid |
| 2 | t_ar_baddebtresult_pkey |  | fid |
