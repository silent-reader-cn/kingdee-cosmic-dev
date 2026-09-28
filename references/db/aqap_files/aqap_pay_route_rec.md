# 业务路由记录-aqap_pay_route_rec

## 业务路由记录-多语言表 t_aqap_pay_route_rec_l

- **表名称：** 业务路由记录-多语言表
- **表名：** t_aqap_pay_route_rec_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_pay_route_rec_l |  | fpkid |
| 2 | idx_pay_route_l |  | fid,flocaleid |

---

## 业务路由记录-主表 t_aqap_pay_route_rec

- **表名称：** 业务路由记录-主表
- **表名：** t_aqap_pay_route_rec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | findividual | 是否对私付款 | varchar | 50 |  | √ | ' ' | 是否对私付款 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsub_biz_type | 子业务类型 | varchar | 50 |  | √ | ' ' | 子业务类型 |
| 7 | fcurrency | 币别 | varchar | 50 |  | √ | ' ' | 币别 |
| 8 | fimpl | 接口实现类 | varchar | 255 |  | √ | ' ' | 接口实现类 |
| 9 | fsource | 数据来源 | varchar | 50 |  | √ | 'system' | 数据来源 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmerge | 是否并笔付款 | varchar | 50 |  | √ | ' ' | 是否并笔付款 |
| 12 | fuse_cn | 付款用途 | varchar | 50 |  | √ | ' ' | 付款用途 |
| 13 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsame_bank | 是否同行付款 | varchar | 50 |  | √ | ' ' | 是否同行付款 |
| 18 | faccprop | 账号属性 | varchar | 1000 |  | √ | ' ' | 账号属性 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fbusconf | 业务配置项 | varchar | 1000 |  | √ | ' ' | 业务配置项 |
| 21 | fsingle | 付款笔数 | varchar | 50 |  | √ | ' ' | 付款笔数 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | furgent | 是否加急付款 | varchar | 50 |  | √ | ' ' | 是否加急付款 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pay_route |  | fbank_version,fsub_biz_type |
| 2 | pk_t_aqap_pay_route_rec |  | fid |
| 3 | idx_impl |  | fimpl |
