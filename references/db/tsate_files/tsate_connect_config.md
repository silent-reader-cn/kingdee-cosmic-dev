# 税企直连设置-tsate_connect_config

## 税企直连设置-主表 t_tsate_connect_config

- **表名称：** 税企直连设置-主表
- **表名：** t_tsate_connect_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | ftaxusername | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 4 | fcreaterld | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsecretkey | 授权秘钥 | varchar | 100 |  | √ | ' ' | 授权秘钥 |
| 8 | flogintype | 登录验证类型 | varchar | 30 |  | √ | ' ' | 登录验证类型,枚举: 0 :无 1 :手机验证码 2 :身份证号码 3 :手工点击 4 :验证码 5 :一卡通 |
| 9 | fmodifierld | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :保存 B :启用 C :禁用 |
| 12 | fbusinessname | 企业名称 | varchar | 200 |  | √ | ' ' | 企业名称 |
| 13 | fconnectuser | 授权用户 | varchar | 100 |  | √ | ' ' | 授权用户 |
| 14 | ftaxno | 税号 | varchar | 100 |  | √ | ' ' | 税号 |
| 15 | ftaxpassword_enp | ftaxpassword_enp | text | 0 |  |  | null |  |
| 16 | fenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用,枚举: 0 :未启用 1 :已启用 |
| 17 | ftaxpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 18 | ftaxtype | 纳税申报类型 | varchar | 30 |  | √ | ' ' | 纳税申报类型,枚举: zzsybnsr :增值税一般纳税人 zzsxgmnsr :增值税小规模纳税人 qysdsjb :企业所得税预缴 qysdsnb :企业所得税汇算清缴 fjsf :附加税费 |
| 19 | fprovince | 省份 | varchar | 30 |  | √ | ' ' | 省份 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_connect_config |  | fid |
| 2 | idx_t_tsate_connect_config |  | ftaxno |
