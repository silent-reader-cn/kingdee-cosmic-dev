# 契税税源信息(暂存)（废弃）-tdm_qishui_dj_tp

## 契税税源信息(暂存)（废弃）-主表 t_tdm_qishui_dj_tp

- **表名称：** 契税税源信息(暂存)（废弃）-主表
- **表名：** t_tdm_qishui_dj_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynumber | 税源编号 | int8 | 64 |  | √ | 0 | 土地税源信息 tdm_tds_basic_info |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdetailaddr | 土地房屋坐落地 | varchar | 50 |  | √ | ' ' | 土地房屋坐落地 |
| 5 | fqszyfs | 权属转移方式 | varchar | 50 |  | √ | ' ' | 权属转移方式,枚举: tucr :土地使用权出让 tdcs :土地使用权出售(包括作价投资入股、偿还债务等应交付经济利益的方式) tdzu :土地使用权赠与(包括以划转、奖励、继承等没有价格的方式) tdhh :土地使用权互换 fwmm :房屋买卖(包括作价投资入股、偿还债务等应交付经济利益的方式) fwzy :房屋赠与(包括以划转、奖励、继承等没有价格的方式) fwhh :房屋互换 |
| 6 | fdealprice | 成交价格 | numeric | 23 | 10 | √ | 0 | 成交价格 |
| 7 | fpgjg | 评估价格 | numeric | 23 | 10 | √ | 0 | 评估价格 |
| 8 | fhtqdrq | 合同签订日期 | timestamp | 0 |  |  | null | 合同签订日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | faffpbl | 按份分配比例 | numeric | 23 | 10 |  | null | 按份分配比例 |
| 11 | fenddate | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcjdj | 成交单价 | numeric | 23 | 10 | √ | 0 | 成交单价 |
| 14 | fsbbbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 16 | fwithheld | 是否代征 | bpchar | 1 |  | √ | '0' | 是否代征 |
| 17 | fsbbstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fqszydxej | 权属转移对象（二级） | varchar | 50 |  | √ | ' ' | 权属转移对象（二级）,枚举: gytd :国有土地 jttd :集体土地 zlf :增量房 clf :存量房 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fjsjg | 计税价格 | numeric | 23 | 10 | √ | 0 | 计税价格 |
| 22 | fsbbapplystatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 declared :申报成功 declaring :申报中 declarefailed :申报失败 |
| 23 | fbillstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fmaindataid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fgyfs | 共有方式 | varchar | 50 |  | √ | ' ' | 共有方式,枚举: ddsy :单独所有 afgy :按份共有 gtgy :共同共有 |
| 28 | fjmxmmcjdm | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 29 | fqszydxsj | 权属转移对象（三级） | varchar | 50 |  | √ | ' ' | 权属转移对象（三级）,枚举: wu :无 zf :住房 fzf :非住房 |
| 30 | fqszydxyj | 权属转移对象（一级） | varchar | 50 |  | √ | ' ' | 权属转移对象（一级）,枚举: tdm_tds_basic_info :土地 tdm_fcs_basic_info :房屋 |
| 31 | fyongtu | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: zzyd :住宅用地 fzzyd :非住宅用地 jzyf :居住用房 fjzyf :非居住用房 |
| 32 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 33 | fgyr | 共有人 | varchar | 50 |  | √ | ' ' | 共有人 |
| 34 | fstartdate | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 35 | fhtbh | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 36 | fsysl | 适用税率 | numeric | 23 | 10 |  | null | 适用税率 |
| 37 | fbdcdydm | 不动产单元代码 | varchar | 50 |  | √ | ' ' | 不动产单元代码 |
| 38 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fqszymj | 权属转移面积 | numeric | 23 | 10 | √ | 0 | 权属转移面积 |
| 40 | fjmlx | fjmlx | varchar | 50 |  | √ | ' ' |  |
| 41 | ftaxoffice | 土地房屋所属主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 42 | fjmbl | 减免比例 | numeric | 23 | 10 | √ | 0 | 减免比例 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_qishui_dj_tp_main |  | fmaindataid |
| 2 | pk_tdm_qishui_dj_tp |  | fid |
