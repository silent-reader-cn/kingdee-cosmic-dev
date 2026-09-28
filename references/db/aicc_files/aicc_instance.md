# 算法部署实例-aicc_instance

## 算法部署实例-主表 t_aicc_instance

- **表名称：** 算法部署实例-主表
- **表名：** t_aicc_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhost | 主机 | varchar | 200 |  | √ | ' ' | 主机 |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fauthurl | 认证URL地址 | varchar | 500 |  | √ | ' ' | 认证URL地址 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | finstancedesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmodelurl | 服务URL地址 | varchar | 500 |  | √ | ' ' | 服务URL地址 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fusersecetkey | 代理用户密钥 | varchar | 512 |  | √ | ' ' | 代理用户密钥 |
| 12 | fserviceid | 所属服务 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 13 | fname | 实例名称 | varchar | 200 |  | √ | ' ' | 实例名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fclientid | ClientID | varchar | 512 |  | √ | ' ' | ClientID |
| 17 | fsecretkey | SecretKey | varchar | 512 |  | √ | ' ' | SecretKey |
| 18 | fmaxparallel | 最大并发数 | int8 | 64 |  | √ | 0 | 最大并发数 |
| 19 | fcustomparam | fcustomparam | varchar | 1024 |  | √ | ' ' |  |
| 20 | fcustomheader | fcustomheader | varchar | 1024 |  | √ | ' ' |  |
| 21 | fprotocol | 协议类型 | varchar | 50 |  | √ | ' ' | 协议类型,枚举: HTTPS :HTTPS WSS :WSS HTTP :HTTP WS :WS |
| 22 | fport | 端口 | int8 | 64 |  | √ | 0 | 端口 |
| 23 | fcontexturl | 上下文地址 | varchar | 500 |  | √ | ' ' | 上下文地址 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fauthtype | 认证方式 | varchar | 50 |  | √ | ' ' | 认证方式,枚举: NONE :无须认证 API2SIGN :摘要认证 OAUTHTOKEN :TOKEN认证 APIKEY :APIKEY BAIDU :BAIDU AWS_SIGN_V4 :亚马逊v4签名认证 TENCENT_HUNYUAN :腾讯混元认证 XUNFEI_SPARK :讯飞星火 XMINDAI :XMINDAI TENCENT_HUNYUAN_PRO_V3 :腾讯混元V3认证 KINGDEE :KINGDEE |
| 26 | fnumber | 实例编码 | varchar | 50 |  | √ | ' ' | 实例编码 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fparalleltype | 并发控制策略 | varchar | 20 |  | √ | ' ' | 并发控制策略,枚举: QPS :QPS RPM :RPM |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_instance_fserviceid |  | fserviceid |
| 2 | pk_t_aicc_instance |  | fentryid |

---

## 算法部署实例-多语言表 t_aicc_instance_l

- **表名称：** 算法部署实例-多语言表
- **表名：** t_aicc_instance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 实例名称 | varchar | 200 |  | √ | ' ' | 实例名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_instance_l_fid |  | fid |
| 2 | pk_t_aicc_instance_l |  | fpkid |
