# 许可同步详情实体-lic_licensesyncdetail

## 许可同步详情实体-主表 t_lic_licsyncdetaillog

- **表名称：** 许可同步详情实体-主表
- **表名：** t_lic_licsyncdetaillog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 用户手机 | varchar | 36 |  | √ | ' ' | 用户手机 |
| 3 | fusername | 用户 | varchar | 255 |  | √ | ' ' | 用户 |
| 4 | fissuccess | 状态 | bpchar | 1 |  | √ | '0' | 状态 |
| 5 | femail | 用户邮箱 | varchar | 100 |  | √ | ' ' | 用户邮箱 |
| 6 | freason | 异常原因 | varchar | 255 |  | √ | ' ' | 异常原因 |
| 7 | fdescription | 操作描述 | varchar | 255 |  | √ | ' ' | 操作描述 |
| 8 | ftaskid | 同步许可任务ID | int8 | 64 |  | √ | 0 | 同步许可任务ID |
| 9 | foperation | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 10 | flogtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: 1 :同步注册用户 2 :下载许可文件 3 :更新许可文件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_licsyncdetaillog |  | fid |
| 2 | ix_licsyncdetaillog_task |  | ftaskid |
