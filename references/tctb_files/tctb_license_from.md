# 税务许可管理-tctb_license_from

## 税务许可管理-主表 t_tctb_license_from

- **表名称：** 税务许可管理-主表
- **表名：** t_tctb_license_from

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivedate | 激活日期 | timestamp | 0 |  |  | null | 激活日期 |
| 3 | fcanceluserid | 注销操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 许可分组 tctb_license_group |
| 5 | flicensestatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :未授权 B :已授权 C :已注销 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcanceldate | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 8 | factiveuserid | 激活操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 10 | fver | 许可版本 | varchar | 50 |  | √ | '3.0' | 许可版本,枚举: 3.0 :3.0许可 4.0 :4.0许可 5.0 :5.0许可 |
| 11 | funifiedsocialcode | 统一社会信用代码 | varchar | 100 |  | √ | ' ' | 统一社会信用代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_license_from |  | forgid,funifiedsocialcode |
| 2 | t_tctb_license_from_pkey |  | fid |
