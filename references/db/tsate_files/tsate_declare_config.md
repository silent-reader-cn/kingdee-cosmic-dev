# 企业税税局登录配置-tsate_declare_config

## 申报表类型-多选基础资料表 t_tsate_template_type

- **表名称：** 申报表类型-多选基础资料表
- **表名：** t_tsate_template_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [模板类型 tctb_template_type](../tctb_files/tctb_template_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_template_type_fk |  | fid |
| 2 | pk_tsate_template_type |  | fpkid |

---

## 企业税税局登录配置-主表 t_tsate_declare_config

- **表名称：** 企业税税局登录配置-主表
- **表名：** t_tsate_declare_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountchecktime | 账密检验时间 | timestamp | 0 |  |  | null | 账密检验时间 |
| 3 | fspecificsubjectlogin | 特定主体登录 | bpchar | 1 |  | √ | '0' | 特定主体登录 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 6 | fnewpage | 新版 | bpchar | 1 |  | √ | '1' | 新版 |
| 7 | fdlsf | 登录身份 | varchar | 50 |  | √ | ' ' | 登录身份,枚举: 0 :财务负责人 1 :办税人 2 :法人/法定代表人 3 :税务代理人 4 :购票员 5 :其他人员 6 :开票员 7 :管理员 8 :社保经纪人 9 :销售人员 10 :领票人 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsynctofpy | 同步至发票云 | bpchar | 1 |  | √ | '0' | 同步至发票云 |
| 10 | ftaxorganid | 税务组织主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 11 | faccountstatus | 账号状态 | varchar | 50 |  | √ | '0' | 账号状态,枚举: 0 :未创建 1 :已创建 2 :已绑定 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcheckresult | 账密检验结果 | varchar | 1000 |  | √ | ' ' | 账密检验结果 |
| 14 | ftaxofficelocation | 申报税局所在地 | int8 | 64 |  | √ | 0 | [税企直连行政区化配置 tsate_areainfo_setting](../tsate_files/tsate_areainfo_setting.md) |
| 15 | fjgport | 机柜端口 | varchar | 50 |  | √ | ' ' | 机柜端口 |
| 16 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftaxusername | 税局登录账号 | varchar | 50 |  | √ | ' ' | 税局登录账号 |
| 19 | fcapassword | CA密码 | varchar | 50 |  | √ | ' ' | CA密码 |
| 20 | fspecificsubjecttype | 特定主体类型 | varchar | 50 |  | √ | '0' | 特定主体类型,枚举: 0 :空 1 :跨区域税源登记纳税人 2 :跨区域报验户 3 :其他登记户 4 :跨省迁出纳税人 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fjghm | 机柜号 | varchar | 50 |  | √ | ' ' | 机柜号 |
| 24 | flogintype | 税局登录验证方式 | varchar | 50 |  | √ | ' ' | 税局登录验证方式,枚举: 1 :短信验证登录 2 :用户名密码登录 3 :CA验证登录 4 :代理人登录 5 :实名登录 6 :普通登录 7 :快捷登录 8 :数字证书登录 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | ftaxmanpassword | 个人用户密码 | varchar | 50 |  | √ | ' ' | 个人用户密码 |
| 27 | fnsrmc | fnsrmc | varchar | 50 |  | √ | ' ' |  |
| 28 | ftelephone | 手机号码 | varchar | 50 |  | √ | ' ' | 手机号码 |
| 29 | ftaxmanname | 个人用户名 | varchar | 50 |  | √ | ' ' | 个人用户名 |
| 30 | fauthorizationcode | 授权码 | varchar | 50 |  | √ | ' ' | 授权码 |
| 31 | flogincategory | 登陆类型 | int8 | 64 |  | √ | 0 | [登陆类型 tsate_login_type](../tsate_files/tsate_login_type.md) |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | ftaxpassword | 税局登录密码 | varchar | 50 |  | √ | ' ' | 税局登录密码 |
| 34 | fvalidatestatus | 税局登录验证状态 | varchar | 50 |  | √ | ' ' | 税局登录验证状态,枚举: 0 :未验证 1 :验证通过 2 :验证失败 3 :验证中 |
| 35 | fvalidatetime | 税局验证时间 | timestamp | 0 |  |  | null | 税局验证时间 |
| 36 | ftaxmansfz | 报税人员身份证 | varchar | 50 |  | √ | ' ' | 报税人员身份证 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | '0' | 同步状态,枚举: 0 :无需同步 1 :成功 2 :失败 3 :待同步 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_declare_config |  | fnsrsbh |
| 2 | pk_tsate_declare_config |  | fid |
