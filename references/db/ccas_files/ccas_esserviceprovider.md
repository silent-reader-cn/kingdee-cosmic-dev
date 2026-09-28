# 电子签章服务商-ccas_esserviceprovider

## 电子签章服务商-多语言表 t_ccas_esignprovider_l

- **表名称：** 电子签章服务商-多语言表
- **表名：** t_ccas_esignprovider_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 服务商全称 | varchar | 255 |  | √ | ' ' | 服务商全称 |
| 3 | fsimplename | 服务商简称 | varchar | 255 |  | √ | ' ' | 服务商简称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_esignprovider_l_fid |  | fid,flocaleid |
| 2 | pk_t_ccas_esignprovider_l |  | fpkid |

---

## 电子签章服务商-主表 t_ccas_esignprovider

- **表名称：** 电子签章服务商-主表
- **表名：** t_ccas_esignprovider

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 服务商全称 | varchar | 255 |  | √ | ' ' | 服务商全称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fbrand | 服务商品牌 | bpchar | 1 |  | √ | '0' | 服务商品牌,枚举: 1 :契约锁 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsimplename | 服务商简称 | varchar | 255 |  | √ | ' ' | 服务商简称 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 服务商ID | varchar | 50 |  | √ | ' ' | 服务商ID |
| 13 | fptinstall | 已安装补丁包 | bpchar | 1 |  | √ | '0' | 已安装补丁包 |
| 14 | fspenable | 启用服务商 | bpchar | 1 |  | √ | '0' | 启用服务商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_esignprovider |  | fid |
| 2 | idx_ccas_esignprovider_no |  | fnumber |

---

## 电子签章服务商-分表 t_ccas_esignprovider_p

- **表名称：** 电子签章服务商-分表
- **表名：** t_ccas_esignprovider_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsecret | 接入密钥（Secret） | varchar | 255 |  | √ | ' ' | 接入密钥（Secret） |
| 3 | fapiserverurl | API接口地址 | varchar | 255 |  | √ | ' ' | API接口地址 |
| 4 | fdecryptsecret | 平台解密秘钥 | varchar | 255 |  | √ | ' ' | 平台解密秘钥 |
| 5 | fapplyappid | 私有化应用ID | int8 | 64 |  | √ | 0 | 私有化应用ID |
| 6 | fcallsecret | 回调解密密钥 | varchar | 255 |  | √ | ' ' | 回调解密密钥 |
| 7 | fcallbackurl | 回调通知地址 | varchar | 1000 |  | √ | ' ' | 回调通知地址 |
| 8 | fappid | 接入令牌（AppId） | varchar | 50 |  | √ | ' ' | 接入令牌（AppId） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ccas_esignprovider_p |  | fid |
| 2 | idx_ccas_esignprovider_appid |  | fappid |
