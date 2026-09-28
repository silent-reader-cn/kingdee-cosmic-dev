# 税局登录配置-tsate_declare_config

## 申报表类型-多选基础资料表 t_tsate_template_type

- **表名称：** 申报表类型-多选基础资料表
- **表名：** t_tsate_template_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
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

## 税局登录配置-主表 t_tsate_declare_config

- **表名称：** 税局登录配置-主表
- **表名：** t_tsate_declare_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fdlsf | 登录身份 | varchar | 50 |  | √ | ' ' | 登录身份,枚举: 0 :财务负责人 1 :办税人 2 :法人/法定代表人 3 :税务代理人 4 :购票员 5 :其他人员 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | ftaxorganid | 申报税局 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fjgport | 机柜端口 | varchar | 50 |  | √ | ' ' | 机柜端口 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftaxusername | 税局登录账号 | varchar | 50 |  | √ | ' ' | 税局登录账号 |
| 12 | fcapassword | CA密码 | varchar | 50 |  | √ | ' ' | CA密码 |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fjghm | 机柜号 | varchar | 50 |  | √ | ' ' | 机柜号 |
| 16 | flogintype | 税局登录验证方式 | varchar | 50 |  | √ | ' ' | 税局登录验证方式,枚举: 1 :短信验证登录 2 :用户名密码登录 3 :CA验证登录 4 :代理人登录 5 :实名登录 6 :普通登录 7 :快捷登录 8 :数字证书登录 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | ftaxmanpassword | 报税人员密码 | varchar | 50 |  | √ | ' ' | 报税人员密码 |
| 19 | fnsrmc | fnsrmc | varchar | 50 |  | √ | ' ' |  |
| 20 | ftelephone | 手机号码 | varchar | 50 |  | √ | ' ' | 手机号码 |
| 21 | ftaxmanname | 报税人员 | varchar | 50 |  | √ | ' ' | 报税人员 |
| 22 | fauthorizationcode | 授权码 | varchar | 50 |  | √ | ' ' | 授权码 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | ftaxpassword | 税局登录密码 | varchar | 50 |  | √ | ' ' | 税局登录密码 |
| 25 | fvalidatestatus | 税局登录验证状态 | varchar | 50 |  | √ | ' ' | 税局登录验证状态,枚举: 0 :未验证 1 :验证通过 2 :验证失败 3 :验证中 |
| 26 | fvalidatetime | 税局验证时间 | timestamp | 0 |  |  | null | 税局验证时间 |
| 27 | ftaxmansfz | 报税人员身份证 | varchar | 50 |  | √ | ' ' | 报税人员身份证 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_declare_config |  | fnsrsbh |
| 2 | pk_tsate_declare_config |  | fid |
