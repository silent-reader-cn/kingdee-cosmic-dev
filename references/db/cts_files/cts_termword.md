# 术语替换-cts_termword

## 术语替换-主表 t_cts_termword

- **表名称：** 术语替换-主表
- **表名：** t_cts_termword

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | flanid | 语言种类 | int8 | 64 |  | √ | 0 | 语言种类 inte_language |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpresetdetailid | 预置术语详情 | int8 | 64 |  | √ | 0 | 预置术语详情 cts_term_preset_detail |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | ftermwordcust | 新名称 | varchar | 80 |  | √ | ' ' | 新名称 |
| 12 | fwordstatus | 术语状态 | varchar | 10 |  | √ | '0' | 术语状态,枚举: 1 :待替换 2 :替换中 3 :已替换 4 :部分替换 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcloudid | 所属云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 15 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | ftermword | 原名称 | varchar | 80 |  | √ | ' ' | 原名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cts_termword_pkey |  | fid |
| 2 | idx_cts_termword_fappid |  | fappid |
