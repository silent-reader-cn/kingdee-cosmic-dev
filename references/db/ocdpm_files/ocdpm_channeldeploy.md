# 渠道促销参数-ocdpm_channeldeploy

## 渠道促销参数-多语言表 t_ocdpm_chldeploy_l

- **表名称：** 渠道促销参数-多语言表
- **表名：** t_ocdpm_chldeploy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_chldeploy_flid |  | fid,flocaleid |
| 2 | pk_ocdpm_chldeploy_l |  | fpkid |

---

## 参数配置-子表 t_ocdpm_chldeployent

- **表名称：** 参数配置-子表
- **表名：** t_ocdpm_chldeployent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontainlowerorg | 包含下级销售组织 | bpchar | 1 |  | √ | '0' | 包含下级销售组织 |
| 3 | forgid | 销售组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fopenautopromotion | 开启自动促销 | bpchar | 1 |  | √ | '0' | 开启自动促销 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmultypromotionstrategy | 多个促销政策执行策略 | bpchar | 1 |  | √ | 'A' | 多个促销政策执行策略,枚举: A :并行全执行 P :执行优先级最高的促销政策 |
| 8 | fopenpromotion | 开启促销 | bpchar | 1 |  | √ | '1' | 开启促销 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_chldeployent_fid |  | fid |
| 2 | pk_ocdpm_chldeployent |  | fentryid |

---

## 渠道促销参数-主表 t_ocdpm_chldeploy

- **表名称：** 渠道促销参数-主表
- **表名：** t_ocdpm_chldeploy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fpromotiondiscountype | 价格&促销折扣订单执行策略 | varchar | 80 |  | √ | ' ' | 价格&促销折扣订单执行策略,枚举: 1 :仅执行促销折扣 2 :促销折扣和价格折扣均执行 3 :执行利于客户的折扣 4 :执行利于企业的折扣 |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_chldeploy_number |  | fnumber |
| 2 | pk_ocdpm_chldeploy |  | fid |
