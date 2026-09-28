# 全网库存共享规则-ocdbd_distributionrules

## 全网库存共享规则-主表 t_ocdbd_distributionrule

- **表名称：** 全网库存共享规则-主表
- **表名：** t_ocdbd_distributionrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbranchid | 发货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 3 | fmodeid | 配送模式 | int8 | 64 |  | √ | 0 | 配送模式 ocdbd_distributionmode |
| 4 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 5 | fcityid | 市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 6 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 7 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 8 | fcountryid | 国家地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 9 | fstockid | 渠道仓库 | int8 | 64 |  | √ | 0 | 渠道仓库 ococic_warehouse |
| 10 | fstockresourceid | 库存资源 | int8 | 64 |  | √ | 0 | 库存资源 ococic_resourcestock |
| 11 | fsalebranchid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 12 | ferpstockid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 13 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcombination | 组合字段 | varchar | 255 |  | √ | ' ' | 组合字段 |
| 16 | fprovinceid | 省 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 17 | fmode | fmode | bpchar | 1 |  | √ | ' ' |  |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | finventoryorgid | 发货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fcountyid | 区 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_distributionrule_com |  | fcombination |
| 2 | pk_ocdbd_distributionrule |  | fid |
| 3 | idx_ocdbd_distributionrule_soc |  | fsaleorgid,fsalebranchid |
