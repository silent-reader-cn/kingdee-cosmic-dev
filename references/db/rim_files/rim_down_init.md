# 全量发票数据同步设置-rim_down_init

## 全量发票数据同步设置-主表 t_rim_down_init

- **表名称：** 全量发票数据同步设置-主表
- **表名：** t_rim_down_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbegin | 下载开始日期 | timestamp | 0 |  |  | null | 下载开始日期 |
| 3 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | foutput_download | 下载进销项类型 | varchar | 50 |  | √ | ' ' | 下载进销项类型,枚举: 1 :进项 2 :销项 3 :进项状态更新 |
| 5 | ftax_no | 纳税人识别号 | varchar | 30 |  | √ | ' ' | 纳税人识别号 |
| 6 | fdown_frequency | 进销项下载频率 | varchar | 50 |  | √ | ' ' | 进销项下载频率,枚举: 5;10;15;20;26 :5号;10号;15号;20号;26号 5;10;15;21;27 :5号;10号;15号;21号;27号 5;10;15;21;28 :5号;10号;15号;21号;28号 5;10;15;21;-1 :5号;10号;15号;21号;月末前一天 |
| 7 | fusestate | 启用状态 | varchar | 2 |  | √ | ' ' | 启用状态 |
| 8 | forg | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fis_check | 进项状态更新的发票是否查验入库 | varchar | 2 |  | √ | ' ' | 进项状态更新的发票是否查验入库,枚举: 1 :进项状态更新获取的发票查验入库 0 :进项状态更新获取的发票只更新状态 2 :进项状态更新获取的发票查验不入库 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | finvoice_type | 下载发票类型 | varchar | 50 |  | √ | ' ' | 下载发票类型,枚举: 2 :电子专用发票 4 :纸质专用发票 3 :纸质普通发票 1 :电子普通发票 5 :普通纸质卷票 15 :通行费电子发票 12 :机动车销售发票 13 :二手车销售发票 21 :海关缴款书 26 :全电普票 27 :全电专票 |
| 14 | ftax_name | 纳税人名称 | varchar | 150 |  | √ | ' ' | 纳税人名称 |
| 15 | fend | 下载结束日期 | timestamp | 0 |  |  | null | 下载结束日期 |
| 16 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_down_init |  | fusestate |
| 2 | pk_rim_down_init |  | fid |

---

## 适用组织分录-子表 t_rim_down_init_userorg

- **表名称：** 适用组织分录-子表
- **表名：** t_rim_down_init_userorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxpayer_name | 纳税人名称 | varchar | 120 |  | √ | ' ' | 纳税人名称 |
| 3 | ftaxpayer_tax_no | 纳税人税号 | varchar | 32 |  | √ | ' ' | 纳税人税号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftaxpayer_org | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_down_init_userorg_fk |  | fid |
| 2 | idx_rim_down_org_taxno |  | ftaxpayer_tax_no |
| 3 | pk_t_rim_down_init_userorg |  | fentryid |
