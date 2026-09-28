# 房间收入信息-tdm_room_revenue

## 房间收入信息-主表 t_tdm_room_revenue

- **表名称：** 房间收入信息-主表
- **表名：** t_tdm_room_revenue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscmj | 实测面积（平方米） | numeric | 23 | 10 | √ | 0 | 实测面积（平方米） |
| 3 | fqsfq | 清算分期 | varchar | 50 |  | √ | ' ' | 清算分期 |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fzgrq | 竣工日期 | timestamp | 0 |  |  | null | 竣工日期 |
| 6 | froomid | 房间编码 | int8 | 64 |  | √ | 0 | 房间基础信息 bastax_room |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fjzmp | 精装/毛坯 | varchar | 50 |  | √ | ' ' | 精装/毛坯,枚举: 0 :精装 1 :毛坯 |
| 10 | fjzmj | 建筑面积（平方米） | numeric | 23 | 10 | √ | 0 | 建筑面积（平方米） |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fqyrq | 签约日期 | timestamp | 0 |  |  | null | 签约日期 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fqybhsze | 签约不含税金额 | numeric | 23 | 10 | √ | 0 | 签约不含税金额 |
| 15 | fbillstatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: D :禁用 A :可用 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fhk | 回款 | numeric | 23 | 10 | √ | 0 | 回款 |
| 18 | fxsyt | 销售业态 | int8 | 64 |  | √ | 0 | 销售业态 bastax_saleformat |
| 19 | fversionid | 版本 | int8 | 64 |  | √ | 0 | 标签设置 tctb_label_group |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fqyhsze | 签约含税金额 | numeric | 23 | 10 | √ | 0 | 签约含税金额 |
| 22 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态 |
| 23 | fkszc | 可售/自持 | varchar | 50 |  | √ | ' ' | 可售/自持,枚举: 0 :可售 1 :自持 |
| 24 | fhz | 货值 | numeric | 23 | 10 | √ | 0 | 货值 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_room_revenue_number |  | fbillno |
| 2 | pk_tdm_room_revenue |  | fid |
