# 核销快照-msmod_wf_sp

## 核销快照-主表 t_msmod_wf_sp

- **表名称：** 核销快照-主表
- **表名：** t_msmod_wf_sp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisplugin | 是否取值插件 | bpchar | 1 |  | √ | '0' | 是否取值插件 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待校验 B :待提交 |
| 4 | fexetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 5 | fverifybillid | 核销单据id | int8 | 64 |  | √ | 0 | 核销单据id |
| 6 | fverifyentrysign | 核销单据分录标识 | varchar | 30 |  | √ | ' ' | 核销单据分录标识 |
| 7 | fverifyqty | 核销数量 | numeric | 23 | 10 | √ | 0 | 核销数量 |
| 8 | fverifybilleid | 核销单据分录id | int8 | 64 |  | √ | 0 | 核销单据分录id |
| 9 | fverifyfield | 核销字段 | varchar | 255 |  | √ | ' ' | 核销字段 |
| 10 | fverifyformid | 核销对象 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_wf_sp |  | fid |
| 2 | idx_t_msmod_wfsp_es |  | fexetime,fstatus |
| 3 | idx_t_msmod_wfsp_fb |  | fverifyformid,fverifybillid |
