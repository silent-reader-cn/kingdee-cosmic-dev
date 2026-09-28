# 税期直连-注册信息-tsate_declare_register

## 税期直连-注册信息-主表 t_tsate_declare_register

- **表名称：** 税期直连-注册信息-主表
- **表名：** t_tsate_declare_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauthorizationcode | 认证码 | varchar | 50 |  | √ | ' ' | 认证码 |
| 3 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | [申报通道 tsate_channel](../tsate_files/tsate_channel.md) |
| 4 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 5 | fchannel | 供应商 | varchar | 50 |  | √ | ' ' | 供应商,枚举: 1 :金蝶 2 :航信 3 :云账房 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_declare_register |  | fnsrsbh |
| 2 | pk_tsate_declare_register |  | fid |
