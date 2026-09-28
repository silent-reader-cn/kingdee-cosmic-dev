# 事件推送订阅-kem_sub_open

## 事件推送订阅-多语言表 t_kem_openeventsub_l

- **表名称：** 事件推送订阅-多语言表
- **表名：** t_kem_openeventsub_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 订阅名称 | varchar | 40 |  | √ | ' ' | 订阅名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 订阅描述 | varchar | 200 |  |  | ' ' | 订阅描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fwebhookname | 回调业务方 | varchar | 20 |  |  | ' ' | 回调业务方 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kem_openeventsub_l |  | fpkid |
| 2 | idx_kem_openeventsub_fid |  | fid,flocaleid |

---

## 事件推送订阅-主表 t_kem_openeventsub

- **表名称：** 事件推送订阅-主表
- **表名：** t_kem_openeventsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequestscript | 请求断言 | varchar | 255 |  |  | ' ' | 请求断言 |
| 3 | fwebhookurl | 回调地址 | varchar | 400 |  | √ | ' ' | 回调地址 |
| 4 | fencryptsecretkey | 加密密钥 | varchar | 200 |  |  | ' ' | 加密密钥 |
| 5 | fisvid | 开发商标识 | varchar | 20 |  | √ | ' ' | 开发商标识 |
| 6 | fwebhookname | fwebhookname | varchar | 20 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fscript | 脚本插件 | varchar | 255 |  |  | ' ' | 脚本插件 |
| 9 | fstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :草稿 B :已发布 F :废弃 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpushtype | 推送方式 | bpchar | 1 |  | √ | '1' | 推送方式,枚举: 1 :Webhook回调 2 :脚本插件 |
| 13 | fversion | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |
| 14 | fname | fname | varchar | 40 |  | √ | ' ' |  |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | ffailovertype | ffailovertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | ffounderid | 初始版本 | int8 | 64 |  | √ | 0 | 初始版本 |
| 19 | fencrypttype | 加密策略 | bpchar | 1 |  |  | ' ' | 加密策略,枚举: 0 :不加密 1 :AES/CBC/PKCS5Padding 2 :SM4/CBC/PKCS5Padding |
| 20 | fencryptlens | 密钥长度(bit) | varchar | 5 |  |  | ' ' | 密钥长度(bit),枚举: 128 :128 |
| 21 | frequestscript_tag | 请求断言_详情 | text | 0 |  |  | ' ' | 请求断言_详情 |
| 22 | fretrytype | 容错类型 | bpchar | 1 |  | √ | ' ' | 容错类型,枚举: 1 :重试3次后挂起 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fsignsecretkey | 签名密钥 | varchar | 200 |  |  | ' ' | 签名密钥 |
| 25 | fscript_tag | 脚本插件_详情 | text | 0 |  |  | ' ' | 脚本插件_详情 |
| 26 | fnumber | 订阅批号 | varchar | 20 |  | √ | ' ' | 订阅批号 |
| 27 | fdesc | fdesc | varchar | 200 |  | √ | ' ' |  |
| 28 | fsigntype | 签名策略 | bpchar | 1 |  |  | ' ' | 签名策略,枚举: 0 :不签名 1 :HMAC_SHA_256 2 :SHA_256 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kem_openeventsub |  | fid |
| 2 | idx_kem_event_opennumber |  | fnumber |

---

## 单据体-子表 t_kem_openeventsubdetl

- **表名称：** 单据体-子表
- **表名：** t_kem_openeventsubdetl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventid | 事件编码 | int8 | 64 |  | √ | 0 | [开放事件 kem_event_open](../kem_files/kem_event_open.md) |
| 3 | feventnumber | feventnumber | varchar | 100 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsubid | 事件订阅 | int8 | 64 |  | √ | 0 | [事件订阅 kem_subscribe](../kem_files/kem_subscribe.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kem_openeventsubdetl |  | fentryid |
| 2 | idx_kem_openeventsubdetl_fid |  | fid |
| 3 | idx_kem_openeventsubdetl_eid |  | feventid |
