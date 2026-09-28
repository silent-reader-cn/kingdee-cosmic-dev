# 配置页面-aiqa_config

## 配置页面-主表 t_aiqa_config

- **表名称：** 配置页面-主表
- **表名：** t_aiqa_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplication | 应用 | varchar | 50 |  | √ | ' ' | 应用 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftokenurl | 获取token地址 | varchar | 300 |  | √ | ' ' | 获取token地址 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fpassword | 解密 | varchar | 50 |  | √ | ' ' | 解密 |
| 10 | ftextfield | 秘钥 | varchar | 500 |  | √ | ' ' | 秘钥 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fphoneurl | 获取手机号地址 | varchar | 300 |  | √ | ' ' | 获取手机号地址 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fprompt_tag | -提示词_详情 | text | 0 |  |  | null | -提示词_详情 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | faccountid | 租户id | varchar | 50 |  | √ | ' ' | 租户id |
| 18 | fprompt | -提示词 | varchar | 255 |  | √ | ' ' | -提示词 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_config_m0 |  | fid |
| 2 | pk_aiqa_config |  | fid |
