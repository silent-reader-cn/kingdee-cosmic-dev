# 云资源应用申请-res_pub_thirdapp_apply

## 云资源应用申请-主表 t_pub_res_app_apply

- **表名称：** 云资源应用申请-主表
- **表名：** t_pub_res_app_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fthirdcode | 开放应用编码 | varchar | 50 |  | √ | ' ' | 开放应用编码 |
| 3 | ftenantid | 当前租户ID | varchar | 50 |  | √ | ' ' | 当前租户ID |
| 4 | faccesstoken | AccessToken认证密钥 | varchar | 256 |  |  | ' ' | AccessToken认证密钥 |
| 5 | fapplytime | fapplytime | timestamp | 0 |  |  | null |  |
| 6 | fsource | 来源 | bpchar | 1 |  | √ | '1' | 来源,枚举: 1 :金蝶云.星瀚 2 :星空旗舰 3 :其他 |
| 7 | fmodifytime | 最后申请时间 | timestamp | 0 |  |  | null | 最后申请时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | finstancenumber | 产品实例编码 | varchar | 100 |  | √ | ' ' | 产品实例编码 |
| 11 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fversion | 版本 | int4 | 32 |  | √ | 1 | 版本 |
| 13 | fremark | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 14 | fname | 开放应用名称 | varchar | 50 |  | √ | ' ' | 开放应用名称 |
| 15 | fphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 申请状态 | bpchar | 1 |  | √ | ' ' | 申请状态,枚举: A :暂存 R :申请中 S :申请成功 F :申请失败 D :禁用 |
| 18 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 上级 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 20 | femail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 21 | faccountname | 当前账套 | varchar | 100 |  | √ | ' ' | 当前账套 |
| 22 | fsecretkey | fsecretkey | varchar | 256 |  | √ | ' ' |  |
| 23 | ffileserver | 文件服务地址 | varchar | 256 |  |  | null | 文件服务地址 |
| 24 | ftargetaccountid | 云端账套ID | varchar | 50 |  | √ | ' ' | 云端账套ID |
| 25 | fappilerusername | 申请人UserName | varchar | 100 |  | √ | ' ' | 申请人UserName |
| 26 | fpublickey | 摘要认证密钥 | varchar | 256 |  | √ | ' ' | 摘要认证密钥 |
| 27 | ftenantname | 当前租户 | varchar | 100 |  | √ | ' ' | 当前租户 |
| 28 | faccountid | 当前账套ID | varchar | 50 |  | √ | ' ' | 当前账套ID |
| 29 | ftargeturl | 连接云端环境 | varchar | 256 |  | √ | ' ' | 连接云端环境,枚举: https://resource.kdcloud.com/ :资源云-生产环境 https://resource.test.kdcloud.com/ :资源云-沙箱环境 https://devtest.kingdee.com:2024/resource_cloud/ :资源云-测试环境 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pub_res_app_apply_num |  | fbillno |
| 2 | pk_t_pub_res_app_apply |  | fid |
