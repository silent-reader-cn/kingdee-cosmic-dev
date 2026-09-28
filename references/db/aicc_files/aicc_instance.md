# 算法部署实例-aicc_instance

## 算法部署实例-主表 t_aicc_instance

- **表名称：** 算法部署实例-主表
- **表名：** t_aicc_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhost | 主机 | varchar | 200 |  | √ | ' ' | 主机 |
| 3 | fname | 实例名称 | varchar | 200 |  | √ | ' ' | 实例名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fclientid | ClientID | varchar | 512 |  | √ | ' ' | ClientID |
| 7 | fsecretkey | SecretKey | varchar | 512 |  | √ | ' ' | SecretKey |
| 8 | fmaxparallel | 最大并发数 | int8 | 64 |  | √ | 0 | 最大并发数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fprotocol | 协议类型 | varchar | 50 |  | √ | ' ' | 协议类型,枚举: HTTPS :HTTPS WSS :WSS HTTP :HTTP WS :WS |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fport | 端口 | int8 | 64 |  | √ | 0 | 端口 |
| 15 | fusersecetkey | 代理用户密钥 | varchar | 512 |  | √ | ' ' | 代理用户密钥 |
| 16 | fcontexturl | 上下文地址 | varchar | 500 |  | √ | ' ' | 上下文地址 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fauthtype | 认证方式 | varchar | 50 |  | √ | ' ' | 认证方式,枚举: NONE :无须认证 API2SIGN :摘要认证 OAUTHTOKEN :TOKEN认证 APIKEY :APIKEY BAIDU :BAIDU AWS_SIGN_V4 :亚马逊v4签名认证 TENCENT_HUNYUAN :腾讯混元认证 XUNFEI_SPARK :讯飞星火 XMINDAI :XMINDAI TENCENT_HUNYUAN_PRO_V3 :腾讯混元V3认证 |
| 19 | fserviceid | 所属服务 | int8 | 64 |  | √ | 0 | 算法服务 aicc_service |
| 20 | fnumber | 实例编码 | varchar | 50 |  | √ | ' ' | 实例编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_instance_fserviceid |  | fserviceid |
| 2 | pk_t_aicc_instance |  | fid |

---

## 算法部署实例-多语言表 t_aicc_instance_l

- **表名称：** 算法部署实例-多语言表
- **表名：** t_aicc_instance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 实例名称 | varchar | 50 |  | √ | ' ' | 实例名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_instance_l_fid |  | fid |
| 2 | pk_t_aicc_instance_l |  | fpkid |
