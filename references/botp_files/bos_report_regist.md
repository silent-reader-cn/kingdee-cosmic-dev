# 监控注册中心-bos_report_regist

## 监控注册中心-主表 t_bos_report_registcenter

- **表名称：** 监控注册中心-主表
- **表名：** t_bos_report_registcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 3 | fmoudlekey | 模块key | varchar | 100 |  | √ | ' ' | 模块key |
| 4 | fcallbackplugin | 回调插件 | varchar | 200 |  |  | null | 回调插件 |
| 5 | fovertime | 超时时间 | int8 | 64 |  | √ | 0 | 超时时间 |
| 6 | fmoudlename | 模块名称 | varchar | 200 |  | √ | ' ' | 模块名称 |
| 7 | fmoudlestatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :禁用 1 :可用 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bos_report_registcenter |  | fid |
| 2 | idx_bos_report_registcenter_m |  | fmoudlekey |
