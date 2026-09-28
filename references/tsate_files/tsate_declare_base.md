# 申报信息基础运维表-tsate_declare_base

## 申报表类型-多选基础资料表 t_tsate_declare_base_type

- **表名称：** 申报表类型-多选基础资料表
- **表名：** t_tsate_declare_base_type

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
| 1 | idx_tsate_declare_base_type_fk |  | fid |
| 2 | pk_tsate_declare_base_type |  | fpkid |

---

## 申报信息基础运维表-主表 t_tsate_declare_base

- **表名称：** 申报信息基础运维表-主表
- **表名：** t_tsate_declare_base

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdeclarechannel | 申报通道 | int8 | 64 |  | √ | 0 | 申报通道 tsate_channel |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fxzqh | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划,枚举: beijing :北京市 tianjin :天津市 hebei :河北省 neimenggu :内蒙古自治区 liaoning :辽宁省 dalian :大连市 jilin :吉林省 heilongjiang :黑龙江省 shanghai :上海市 jiangsu :江苏省 zhejiang :浙江省 ningbo :宁波市 anhui :安徽省 fujian :福建省 xiamen :厦门市 jiangxi :江西省 shandong :山东省 qingdao :青岛市 henan :河南省 hubei :湖北省 hunan :湖南省 guangdong :广东省 shenzhen :深圳市 guangxi :广西壮族自治区 hainan :海南省 chongqing :重庆市 sichuan :四川省 guizhou :贵州省 yunnan :云南省 xizang :西藏藏族自治区 shaanxi :陕西省 shanxi :山西省 gansu :甘肃省 qinghai :青海省 ningxia :宁夏回族自治区 xinjiang :新疆维吾尔自治区 |
| 7 | flogintype | 税局验证方式 | varchar | 50 |  | √ | ' ' | 税局验证方式,枚举: 1 :短信验证登录 2 :用户名密码登录 3 :CA验证登录 4 :代理人登录 5 :实名登录 6 :普通登录 7 :快捷登录 8 :数字证书登录 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fisspecial | 是否特殊地区 | bpchar | 1 |  | √ | ' ' | 是否特殊地区 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ftaxorganid | 申报税局 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fissystem | 系统预制 | varchar | 50 |  | √ | ' ' | 系统预制,枚举: 0 :否 1 :是 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fchannel | 接口商 | varchar | 50 |  | √ | ' ' | 接口商,枚举: 1 :金蝶账无忧 3 :神州云合 4 :广州电子税局 5 :云账房 6 :广西税局 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_base |  | fid |
| 2 | idx_tsate_declare_base |  | fbillno |
